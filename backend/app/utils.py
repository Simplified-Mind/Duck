import pandas as pd
from collections import OrderedDict
from typing import Optional, Literal, Union, List, Callable, Any, Hashable, Iterable, Tuple, Set
from dataclasses import dataclass, asdict
from fastapi import HTTPException, status
from functools import wraps, partial
from traceback import format_exc

ALIGN = Literal['left', 'center', 'right']
SHOW_OVERFLOW = Literal['ellipsis', 'title', 'tooltip']


@dataclass
class Cell:
    field: str
    align: Optional[str] = 'left'
    tooltip: Optional[str] = None
    background_color: Optional[str] = None
    color: Optional[str] = None
    class_name: Optional[str] = None
    show_overflow: Optional[Union[bool, SHOW_OVERFLOW]] = True


@dataclass
class Grid:
    """
    vxe-grid wrapper
    Ref: https://x-extends.github.io/vxe-table/#/grid/api
    """
    columns: List[dict]
    data: List[dict]
    auto_resize: Optional[bool] = False
    stripe: Optional[bool] = False
    border: Optional[Union[bool, Literal['default', 'full', 'outer', 'inner', 'none']]] = True
    round: Optional[bool] = False
    size: Optional[Literal['medium', 'small', 'mini']] = None
    align: Optional[ALIGN] = 'left'
    header_align: Optional[ALIGN] = 'left'
    footer_align: Optional[ALIGN] = 'left'
    resizable: Optional[bool] = True
    show_overflow: Optional[Union[bool, SHOW_OVERFLOW]] = True
    show_header: Optional[bool] = False
    show_header_overflow: Optional[Union[bool, SHOW_OVERFLOW]] = True
    show_footer_overflow: Optional[Union[bool, SHOW_OVERFLOW]] = True
    highlight_current_row: Optional[bool] = False
    highlight_hover_row: Optional[bool] = False
    highlight_current_column: Optional[bool] = False
    highlight_hover_column: Optional[bool] = False
    merge_cells: Optional[List[dict]] = None
    merge_footer_items: Optional[List[dict]] = None
    keep_source: Optional[bool] = True
    height: Optional[Union[str, int]] = None
    max_height: Optional[Union[str, int]] = None
    row_id: Optional[str] = None
    column_key: Optional[bool] = False
    row_key: Optional[bool] = False
    custom_config: Optional[dict] = None
    print_config: Optional[dict] = None
    sort_config: Optional[dict] = None
    filter_config: Optional[dict] = None
    pager_config: Optional[dict] = None
    form_config: Optional[dict] = None
    toolbar_config: Optional[dict] = None
    proxy_config: Optional[dict] = None
    import_config: Optional[dict] = None
    export_config: Optional[dict] = None
    checkbox_config: Optional[dict] = None
    edit_rules: Optional[dict] = None
    edit_config: Optional[dict] = None


class Node(dict):
    def __init__(self, uid: Hashable):
        self._parent = None            # pointer to parent Node

        # keep reference to uid
        self['field'] = uid
        self['title'] = uid

        self['children'] = []          # collection of pointers to child Nodes

    @property
    def parent(self):
        return self._parent            # return the object at the _parent pointer

    @parent.setter
    def parent(self, node):
        self._parent = node
        self['field'] = f'{node["field"]}@{self["field"]}'
        node['children'].append(self)  # add this node to parent's list of children


def build(pairs: Iterable[Tuple[Hashable, Hashable]]) -> dict:
    tree = {}
    for pid, uid in pairs:          # check if the node was already added, else add
        child = tree.get(uid)
        if child is None:
            child = Node(uid)       # create child node
            tree[uid] = child       # add the node to the tree, using the uid as key

        if uid != pid:
            # set node.parent pointer to where the parent is
            parent = tree.get(pid)
            if parent is None:
                parent = Node(pid)  # create parent if missing
                tree[pid] = parent
            child.parent = parent
    return tree


def get_pairs(lst: list, n: int) -> List[Tuple[Hashable, Hashable]]:
    step = 2
    pairs = OrderedDict()
    for x in lst:
        for i in range(n - 1):
            pairs.update({x[i: i + step: 1]: None})

    return list(pairs)


def grid_config(func: Optional[Callable] = None, index: Optional[bool] = True, **opts) -> dict:
    # Convert dataframe to vxe-grid columns and data objects
    if func is None:
        return partial(grid_config, index=index, **opts)

    def get_content(df: pd.DataFrame, names: Optional[Set[str]] = None) -> Tuple[List[dict]]:
        n = df.columns.nlevels
        merge_cells = []
        if n > 1:
            columns = []
            for i, (x, y) in enumerate(df.groupby(axis=1, level=0, sort=False)):
                pairs = get_pairs(y.columns.to_flat_index(), n)
                tree = build(pairs)
                result = tree[x]

                if names and set(x).intersection(names):
                    result['title'] = ''

                    # groupby consecutive values
                    merge_cells += [
                        {'row': b.index.min(), 'col': i, 'rowspan': b.size, 'colspan': 1}
                            for a, b in y.groupby([(y[x] != y[x].shift()).cumsum()])
                    ]

                columns.append(result)
            df.columns = ['@'.join(x) for x in df.columns.to_flat_index()]
        else:
            columns = [{'title': x, 'field': x} for x in df.columns]

        data = df.to_dict('records')
        return columns, data, merge_cells

    @wraps(func)
    def wrapper(*args, **kwargs) -> dict:
        df = func(*args, **kwargs)
        names = None
        if index:
            names = set(df.index.names)
            df = df.reset_index()

        columns, data, merge_cells = get_content(df, names)
        return Grid(columns=columns, data=data, merge_cells=merge_cells, **opts)

    return wrapper


def catch(func: Callable) -> Any:
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=format_exc()
            )
    return inner



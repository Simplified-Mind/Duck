import pandas as pd
from typing import Optional, Literal, Union, List, Callable, Any, Dict
from dataclasses import dataclass
from fastapi import HTTPException, status
from functools import wraps
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


def get_grid_config(df: pd.DataFrame) -> Dict[str, List[dict]]:
    # Convert dataframe to vxe-grid columns and data objects
    columns = df.columns.tolist()
    data = df.to_dict('records')
    return dict(columns=columns, data=data)


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



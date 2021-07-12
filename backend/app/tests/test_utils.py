from pytest import main
import numpy as np
import pandas as pd
from backend.app.utils import grid_config


df = pd.DataFrame(
    {
        'A': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'one', 'two', 'two', 'one', 'one', 'two', 'two'],
        'C': ['small', 'large', 'large', 'small', 'small', 'large', 'small', 'small', 'large'],
        'D': [1, 2, 2, 3, 3, 4, 5, 6, 7],
        'E': [2, 4, 5, 5, 6, 6, 8, 9, 9],
        'F': [2, 4, 5, 5, 6, 6, 8, 9, 9]
    }
)

pt = pd.pivot_table(
    df,
    values=['D', 'E'],
    index=['A', 'C', 'F'],
    aggfunc={'D': np.mean, 'E': [min, max, np.mean]}
)


def test_pivot_table_with_index():
    @grid_config(keep_source=False)
    def dummy():
        return pt

    result = dummy()
    r, _ = pt.shape
    assert len(result.data) == r
    assert result.keep_source is False
    assert len(result.columns) == 5
    assert len(result.merge_cells) == 15
    assert len(result.columns[-2]['children']) == 1
    assert len(result.columns[-1]['children']) == 3
    assert result.columns[-2]['children'][0]['field'] == 'D@mean'
    assert {x['field'] for x in result.columns[-1]['children']} == {'E@max', 'E@mean', 'E@min'}


def test_pivot_table_without_index():
    @grid_config(index=False)
    def dummy():
        return pt

    result = dummy()
    r, _ = pt.shape
    assert len(result.data) == r
    assert len(result.columns) == 2
    assert result.merge_cells == []
    assert result.keep_source is True


if __name__ == '__main__':
    main()

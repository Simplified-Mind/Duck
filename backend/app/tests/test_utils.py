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


def test_pivot_table():
    @grid_config
    def dummy():
        return pd.pivot_table(
            df,
            values=['D', 'E'],
            index=['A', 'C', 'F'],
            aggfunc={'D': np.mean, 'E': [min, max, np.mean]}
        )

    result = dummy()
    assert len(result['columns']) == 2
    assert len(result['columns'][0]['children']) == 1
    assert len(result['columns'][1]['children']) == 3
    assert result['columns'][0]['children'][0]['field'] == 'mean'
    assert {x['field'] for x in result['columns'][1]['children']} == {'max', 'mean', 'min'}


if __name__ == '__main__':
    test_pivot_table()

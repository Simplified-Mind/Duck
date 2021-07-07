import pandas as pd
from backend.app.utils import get_grid_config


df = pd.DataFrame(
    {
        'A': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'one', 'two', 'two', 'one', 'one', 'two', 'two'],
        'C': ['small', 'large', 'large', 'small', 'small', 'large', 'small', 'small', 'large'],
        'D': [1, 2, 2, 3, 3, 4, 5, 6, 7],
        'E': [2, 4, 5, 5, 6, 6, 8, 9, 9]
    }
)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

WINE_TYPE_ENCONDING = {
    'red': 0,
    'white': 1
}

def load_data(*paths: list[str],
              delimiter: str = ';') -> list[pd.DataFrame]:
    dfs = [pd.read_csv(path, delimiter=delimiter) for path in paths]
    print('Files loaded: {}\n'.format(
        '\n'.join([path for path in paths])))
    return dfs

def create_wine_type_feature(df: pd.DataFrame,
                             wine_type: str) -> pd.DataFrame:
    df['type'] = wine_type
    print('Type feature created for {} type'.format(wine_type))
    return df

def join_wine_dataframes(*dfs: list[pd.DataFrame]) -> pd.DataFrame:
    wine = pd.concat(dfs, ignore_index=True)
    print('Dataframes joined')
    return wine

def encode_wine_type(data: pd.DataFrame,
                     encoding: dict[str, int] = WINE_TYPE_ENCONDING
    ) -> pd.DataFrame:
    df = data.copy()
    df['type'] = df['type'].map(encoding)
    print('Type feature encoded')
    return df

def split_dataset(df: pd.DataFrame,
                  train_size: float = 0.8
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
    return train_test_split(df, train_size=train_size)

def standard_scale(data: pd.DataFrame,
                   columns_to_transform: list[str]) -> pd.DataFrame:
    df = data.copy()
    df[columns_to_transform] = df[columns_to_transform].apply(
        lambda col: (col - col.mean) / col.std(), axis=1
    )
    return df

def log_normalize(data: pd.DataFrame,
                  columns_to_transform: list[str]) -> pd.DataFrame:
    df = data.copy()
    df[columns_to_transform] = df[columns_to_transform].apply(
        lambda col: np.log(col), axis=1
    )
    return df

import pandas as pd
import os

def write_csv(data: pd.DataFrame,
              directory: str,
              filename: str) -> None:
    print('CSV writing in progress...')
    if '.csv' not in filename[-4:]:
        filename += '.csv'
    filepath = os.path.join(directory, filename)
    data.to_csv(filepath, index=False)
    print('CSV {} wrote in to {}'.format(filename, directory))
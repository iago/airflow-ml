import os
from preprocessing import load_data, create_wine_type_feature, \
    encode_wine_type, join_wine_dataframes
from utils import write_csv

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, 'data', 'raw')
RED_WINE_PATH = os.path.join(DATA_DIR, 'winequality-red.csv')
WHITE_WINE_PATH = os.path.join(DATA_DIR, 'winequality-red.csv')

def make_dataset(destination_directory: str = None,
                 destination_filename: str = None) -> None:
    print('Making dataset')
    red_wine, white_wine = load_data(RED_WINE_PATH, WHITE_WINE_PATH)
    red_wine = create_wine_type_feature(red_wine, 'red')
    white_wine = create_wine_type_feature(white_wine, 'white')
    wine = join_wine_dataframes(red_wine, white_wine)
    wine = encode_wine_type(wine)
    if (destination_directory is not None 
            and destination_filename is not None):
        write_csv(wine, destination_directory, destination_filename)
    print('Dataset making complete')

if __name__ == '__main__':
    make_dataset()
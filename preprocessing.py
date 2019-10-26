import pandas as pd
import os

DATASETS = os.path.join('datasets')


def data(file_path: str):
    csv_path = os.path.join(DATASETS, file_path)
    return pd.read_csv(csv_path)

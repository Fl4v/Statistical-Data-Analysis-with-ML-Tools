import pandas as pd
from sklearn.model_selection import train_test_split
import os

DATASETS = os.path.join('datasets')


def data(file_path: str):
    csv_path = os.path.join(DATASETS, file_path)
    return pd.read_csv(csv_path)


def split_train_test_data(data_frame):
    train_set, test_set = train_test_split(data(data_frame), test_size=0.2, random_state=42)
    return train_set, test_set

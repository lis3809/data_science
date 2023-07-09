import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None) # отобразить все колонки

from scipy import stats

if __name__ == '__main__':
    df = pd.read_csv("C:/Users/STELS/PycharmProjects/data_science_1t/task_1.5/diabetes_prediction_dataset.csv")
    df = df.loc[df.gender != 'Other']
    print(df.gender.value_counts())
import numpy as np
import pandas as pd

# Creating a sample data
data = {'Score': [25, np.nan, 30, np.nan, 29, 27, 32, 31]}
df = pd.DataFrame(data)

# Mean Imputation
df['Score_Mean'] = df['Score'].fillna(df['Score'].mean())

# Median Imputation
df['Score_Median'] = df['Score'].fillna(df['Score'].median())

# Mode Imputation
df['Score_Mode'] = df['Score'].fillna(df['Score'].mode()[0])

print(df)
from sklearn.impute import KNNImputer

# Assuming the same initial data with missing values
data = {'Feature1': [25, 20, 30, 40, 29, 27, 32, 31],
        'Feature2': [20, 25, np.nan, 45, 30, 25, 35, 40]}
df = pd.DataFrame(data)

# Predictive Imputation using KNN
imputer = KNNImputer(n_neighbors=2)
df_filled = imputer.fit_transform(df)

print(df_filled)
import pandas as pd

# Let's assume a time series data with missing values
time_data = {'Time': pd.date_range(start='1/1/2023', periods=8, freq='D'),
             'Value': [1, np.nan, np.nan, 4, 5, np.nan, 7, 8]}
df_time = pd.DataFrame(time_data)

# LOCF
df_time['Value_LOCF'] = df_time['Value'].fillna(method='ffill')

# NOCB
df_time['Value_NOCB'] = df_time['Value'].fillna(method='bfill')

print(df_time)
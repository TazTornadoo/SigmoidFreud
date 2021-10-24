import pandas as pd
import sqlite3

conn = sqlite3.connect("SigmoidFreud", check_same_thread=False)

df_X_train = pd.read_csv("/workspaces/SigmoidFreud/Data/X_train_window_size_5_time_encoding_True.csv", sep=',')
df_X_train.to_sql("X_train_window_size_5_time_encoding_True", conn, if_exists="replace", index=False)

df_X_valid = pd.read_csv("/workspaces/SigmoidFreud/Data/X_valid_window_size_5_time_encoding_True.csv", sep=',')
df_X_valid.to_sql("X_valid_window_size_5_time_encoding_True", conn, if_exists="replace", index=False)

df_X_test = pd.read_csv("/workspaces/SigmoidFreud/Data/X_test_window_size_5_time_encoding_True.csv", sep=',')
df_X_test.to_sql("X_test_window_size_5_time_encoding_True", conn, if_exists="replace", index=False)

df_X_train_15 = pd.read_csv("/workspaces/SigmoidFreud/Data/X_train_window_size_15_time_encoding_True.csv", sep=',')
df_X_train_15.to_sql("X_train_window_size_15_time_encoding_True", conn, if_exists="replace", index=False)

df_X_valid_15 = pd.read_csv("/workspaces/SigmoidFreud/Data/X_valid_window_size_15_time_encoding_True.csv", sep=',')
df_X_valid_15.to_sql("X_valid_window_size_15_time_encoding_True", conn, if_exists="replace", index=False)

df_X_test_15 = pd.read_csv("/workspaces/SigmoidFreud/Data/X_test_window_size_15_time_encoding_True.csv", sep=',')
df_X_test_15.to_sql("X_test_window_size_15_time_encoding_True", conn, if_exists="replace", index=False)

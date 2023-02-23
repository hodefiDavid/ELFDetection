
# Imports, settings and first dataset view

import elf2Jason as e2j
import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split


df_bad = pd.read_pickle("packed_df.pkl")
print(df_bad.head)
df_good = pd.read_pickle("packed_good_df.pkl")
print(df_good.head)

X = pd.concat([df_bad, df_good], axis=0)

arr1 = np.full(shape=2574, fill_value="bad")
arr2 = np.full(shape=256, fill_value="good")
arr = np.concatenate((arr1, arr2))
y = np.stack(arr)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1765, random_state=42, stratify=y)

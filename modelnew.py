
# Imports, settings and first dataset view

# import elf2Jason as e2j
# import pandas as pd
# import numpy as np
# import json
# from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
import numpy as np
import json
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

# This is our main preprocessing function that will iterate over all of the chosen 
# columns and run some feature extraction models
def vectorize_df(df):
    le = LabelEncoder()
    h_vec = HashingVectorizer(n_features=4)
    # Run LabelEncoder on the chosen features
    for column in df.columns: 
        df[column] = h_vec.fit_transform(df[column])

    return df

df_bad = pd.read_pickle("packed_bad_df_dict.pkl")
# print(df_bad.head)
df_good = pd.read_pickle("packed_good_df_dict.pkl")
# print(df_good.head)

X = pd.concat([df_bad, df_good], axis=0)

arr1 = np.full(shape=2550, fill_value="bad")
arr2 = np.full(shape=256, fill_value="good")
arr = np.concatenate((arr1, arr2))
y = np.stack(arr)
print(y)

X = vectorize_df(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1765, random_state=42, stratify=y)


# Fit a linear regression model to the expanded DataFrame
# model = LinearRegression()
# X = df_expanded.drop('y', axis=1)
# y = df_expanded['y']
# model.fit(X, y)


# We choose our model of choice and set it's hyper parameters you can change anything
clf = RandomForestClassifier(n_estimators=100)

# Train Model
clf.fit(X_train, y_train)

# Check data balance and variety
print(sorted(Counter(y_train).items()))
# We print our results
sns.set(rc={'figure.figsize': (15, 8)})
randomForestClassifier_predictions = clf.predict(X_test)
true_labels = y_test
cf_matrix = confusion_matrix(true_labels, randomForestClassifier_predictions)
clf_report = classification_report(true_labels, randomForestClassifier_predictions, digits=5)
heatmap = sns.heatmap(cf_matrix, annot=True, cmap='Blues', fmt='g',
                      xticklabels=np.unique(true_labels),
                      yticklabels=np.unique(true_labels))

# The heatmap is cool but this is the most important result
print(clf_report)

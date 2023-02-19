# Imports, settings and first dataset view
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


def load_dataset_train(dataset_file):
    # Set pandas to show all columns when you print a dataframe
    pd.set_option('display.max_columns', None)

    # Read the json and read it to a pandas dataframe object, you can change these settings
    with open("combined.json") as file:
        raw_ds = json.load(file)
    # result = pd.DataFrame.from_records(json.load(file))
    df_load = pd.json_normalize(raw_ds)

    # Shoe the first five lines of the dataframe to see if everything was read accordingly
    print(df_load.head())
    # print(result.head())

    print("load_dataset_train successfully")
    # return result



def Fill_black_attack_with_Benign(df):
    # Fill the black attack tag lines with "Benign" string
    df['request.Attack_Tag'] = df['request.Attack_Tag'].fillna('Benign')
    df['attack_type'] = df['request.Attack_Tag']
    print("Fill_black_attack_with_Benign successfully")
    return df


# This function will be used in the lambda below to iterate over the label columns
# You can use this snippet to run your own lambda on any data with the apply() method
def categorize(row):
    if row['request.Attack_Tag'] == 'Benign':
        return 'Benign'
    return 'Malware'


# Remove all NAN columns or replace with desired string
# This loop iterates over all of the column names which are all NaN
def renove_nan_columns(df):
    for column in df.columns[df.isna().any()].tolist():
        # df.drop(column, axis=1, inplace=True)
        df[column] = df[column].fillna('None')

    print("renove_nan_columns successfully")
    return df


dataset_file = "./combined.json"
df = load_dataset_train(dataset_file)
# df = Fill_black_attack_with_Benign(df)
# df[test_type] = df.apply(lambda row: categorize(row), axis=1)
# # After finishing the arrangements we delete the irrelevant column
# df.drop('request.Attack_Tag', axis=1, inplace=True)
# df = renove_nan_columns(df)

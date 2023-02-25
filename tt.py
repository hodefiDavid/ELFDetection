# '/home/david/elf/testelf/0-avelf'

import random
import streamlit as st
import math
import joblib
import subprocess
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from collections import Counter
import seaborn as sns
import numpy as np
import joblib
from sklearn.feature_extraction.text import CountVectorizer

def get_elf_reader(file_path):
    cmd = ['readelf', '-a', file_path]
    output = subprocess.check_output(cmd, universal_newlines=True)
    return output

fileAddress = '/home/david/elf/testelf/0-avelf'
loaded_model = joblib.load('model.joblib')
t = []
print("got the file : \n",fileAddress)
elf = get_elf_reader(fileAddress)
    # print("elf file = \n",elf)
t.append(elf)
    # Create a CountVectorizer object to convert the text data into feature vectors
vectorizer = CountVectorizer()

    # Use the CountVectorizer object to fit and transform the training data
elf_vectors = vectorizer.fit_transform(t)

res = loaded_model.predict(elf_vectors)

print("res = ", res)
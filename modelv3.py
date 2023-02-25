import subprocess
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from collections import Counter
import seaborn as sns
import numpy as np
import joblib


def get_elf_reader(file_path):
    cmd = ['readelf', '-a', file_path]
    output = subprocess.check_output(cmd, universal_newlines=True)
    return output
# print(get_elf_reader('/home/david/ELFDetection/ELFDetection/training-sample'))



from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Define the training data
train_data = []
# Define the test data
test_data = []
train_labels = []


train_folder = '/home/david/elf/VirusShare_ELF_20140617'
for f in os.listdir(train_folder):
    try:
        tmp_data = get_elf_reader(os.path.join(train_folder, f))
        train_data.append(tmp_data)
        # Define the labels for the training data
        train_labels.append("bad")
    except:
        continue

train_folder = '/home/david/ELFDetection/ELFDetection/output'
for f in os.listdir(train_folder):
    try:
        tmp_data = get_elf_reader(os.path.join(train_folder, f))
        train_data.append(tmp_data)
        # Define the labels for the training data
        train_labels.append("good")
    except:
        continue

# Define the test data
test_data = []

train_folder = '/home/david/elf/testelf'
for f in os.listdir(train_folder):
    try:
        tmp_data = get_elf_reader(os.path.join(train_folder, f))
        test_data.append(tmp_data)
        # Define the labels for the training data
        # train_labels.append("bad")
    except:
        continue



# Create a CountVectorizer object to convert the text data into feature vectors
vectorizer = CountVectorizer()

# Use the CountVectorizer object to fit and transform the training data
train_vectors = vectorizer.fit_transform(train_data)

X_train, X_test, y_train, y_test = train_test_split(train_vectors, train_labels, test_size=0.1765, random_state=42, stratify=train_labels)


# We choose our model of choice and set it's hyper parameters you can change anything
# clf = RandomForestClassifier(n_estimators=100)
# Train a Multinomial Naive Bayes classifier on the training data
clf = MultinomialNB()
# clf.fit(train_vectors, train_labels)

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


# Save the model to a file
joblib.dump(clf, 'model.joblib')

# # Load the model from the file
# loaded_model = joblib.load('model.joblib')
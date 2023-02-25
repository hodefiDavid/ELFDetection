import os
import pandas as pd
from elftools.elf.elffile import ELFFile
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Function to load ELF file into pandas dataframe
def elf_to_df(filepath):
    with open(filepath, 'rb') as f:
        try:
            elffile = ELFFile(f)
        # Load section data into dictionary
            sections = {}
            for section in elffile.iter_sections():
                sections[section.name] = section.data()
        # Create dataframe from dictionary
            df = pd.DataFrame.from_dict(sections, orient='index').transpose()
            return df

        except:
            return ""

# Load training data
train_folder = '/home/david/elf/VirusShare_ELF_20140617'
train_data_list = []
for f in os.listdir(train_folder):
    tmp_data = elf_to_df(os.path.join(train_folder, f))
    if type(tmp_data) != type(""):
        train_data_list.append(tmp_data)
train_data = pd.concat(train_data_list, ignore_index=True)

# Preprocess training data
# train_data = train_data[['section_name_1', 'section_name_2', 'section_name_3', 'target']]
train_data = train_data[train_data.columns, 'target']
encoder = OneHotEncoder()
X = encoder.fit_transform(train_data.drop('target', axis=1))
y = train_data['target']

# Split training data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Load test data (i.e., ELF files to make predictions on)
test_folder = '/home/david/elf/testelf'
test_data = []
for f in os.listdir(test_folder):
    datatmp = elf_to_df(os.path.join(test_folder, f))
    if type(datatmp) != type(""):
        test_data.append(test_data) 
# Preprocess test data
test_data = pd.concat(test_data, ignore_index=True)
# test_data = test_data[['section_name_1', 'section_name_2', 'section_name_3']]
test_data = test_data[test_data.columns]

X_test = encoder.transform(test_data)

# Make predictions on test data
predictions = model.predict(X_test)

# Save predictions to file
output_file = '/predictions.csv'
pd.DataFrame(predictions).to_csv(output_file, index=False, header=False)
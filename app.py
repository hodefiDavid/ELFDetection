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

# from sklearn.externals import joblib
import time
from PIL import Image
# Load the model from the file
def load_model(file_name):
  loaded_model = joblib.load(file_name)
  return loaded_model

def load_images(file_name):
  img = Image.open(file_name)
  return st.image(img,width=300)

def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)
# need to change to our actual code

def algo_to_det(fileAddress,model)-> int:
  
  try:
    t = []
    print("got the file : \n",fileAddress)
    elf = get_elf_reader(fileAddress)
    # print("elf file = \n",elf)
    t.append(elf)
    # Create a CountVectorizer object to convert the text data into feature vectors
    vectorizer = CountVectorizer()

    # Use the CountVectorizer object to fit and transform the training data
    elf_vectors = vectorizer.fit_transform(t)

    res = model.predict(elf_vectors)

    print("res = ", res)
    if res == 'good':
       return 1
    else:
       return -1
  except:
    #  if somthing got worng we will return bad file
    return -1 



def main(model):
  """ELF Classifier App
    With Streamlit

  """

  st.title("ELF Classifier")
  html_temp = """
  # <div style="background-color:blue;padding:10px">
  # <h2 style="color:grey;text-align:center;">Streamlit App </h2>
  # </div>

  """
  st.markdown(html_temp,unsafe_allow_html=True)
#   load_css('icon.css')
#   load_icon('people')

  fileAddress = st.text_input('Input your text here:')

  
  if st.button("Predict"):
    result = algo_to_det(fileAddress,model)
    if result < 1:
      prediction = 'Bad'
      img = 'mal.png'
    else:
      prediction = 'Good'
      img = 'ben.jpeg'

    # st.success('The data: file size: {}'.format(file_size)) #: {}' ) #sent packets: {}\trevive packets {}\t douratrion:{} \nwas classified as {}'.format(sent_packets,recive_packets,duration,prediction))
    load_images(img)

print("#hetchalnu")
loaded_model = load_model('model.joblib')
main(loaded_model)

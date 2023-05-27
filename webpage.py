import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import pickle
import warnings
warnings.filterwarnings('ignore')

# Load the pickle models
model = pickle.load(open('model(1).pkl', 'rb'))
df = pickle.load(open('data(1).pkl', 'rb'))

html_temp = """ 
<div style = "background-color: #70d4bc; padding: 10px">
<h2 style = "color: white; text-align: center;">Heart Disease Prediction
</div>
<div style = "background-color: white; padding: 5px">
<p style= "color: #7c4deb; text-align: center; font-family: Courier; font-size: 15px;">
<i>Get an idea of the presence of heart disease.</i></p>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

image_path = 'img.jpg'
image = Image.open(image_path)
st.image(image, use_column_width=True)


# Define the features
# slope
slope = st.selectbox('Slope', ['1 (Upsloping)','2 (Flat)','3 (Downsloping)'])
# thal
thal = st.selectbox('Thalassemia', ['0 (Normal)','1 (Fixed defect)','2 (Reversible defect)'])
# rbs
rbs = st.slider('Resting blood sugar', 94, 180)
# chest_pain
chest_pain = st.selectbox('Chest pain', ['1 (Typical Angina)','2 (Atypical Angina)','3 (Non-Anginal pain)','4 (Asmyptomatic)'])
# vessels
vessels	= st.selectbox('Vessels', df['vessels'].unique())
# fasting_blood_sugar
fbs = st.selectbox('Fasting blood sugar', ['Greater than 120mg/ml', 'Lower than 120mg/ml'])
# resting_ekg
resting_ekg = st.selectbox('Resting  electrocardiographic measurement', ['0 (Normal)','1 (STT Abnormality)','2 (Hypertrophy)'])
# cholesterol
cholesterol = st.slider('Cholesterol', 126, 564)
# depression
depression = st.slider('Depression', 0.0, 6.2)
# sex
sex = st.selectbox('Sex', ['Male', 'Female'])
# age
age = st.slider('Age', 29, 77)
# heart_rate
heart_rate = st.slider('Heart rate', 96, 202)
# angina
angina = st.selectbox(' Exercise-induced Angina', ['Yes', 'No'])


# Get the inputs
inputs = [[slope,thal,rbs,chest_pain,vessels,fbs,resting_ekg,cholesterol,depression,sex,age,heart_rate,angina]]
features = pd.DataFrame(inputs, index=[0])
features.columns = ['Slope','Thal','Resting blood sugar','Chest Pain','Vessels','Fasting blood sugar','Resting ekg',
                    'Cholesterol','Depression','Sex','Age','Heart Rate','Angina']
st.markdown('##### Selected parameters')
st.write(features)


def classify(num):
    if (num == 0):
        return 'Heart Disease not present.'
    elif (num == 1):
        return 'Heart Disease present. Seek treatment!!'

# Predict
def prediction():
    if (st.button('Predict')):
        query = np.array([
            slope,thal,rbs,chest_pain,vessels,fbs,resting_ekg,cholesterol,depression,sex,age,heart_rate,angina
        ], dtype=object)
        query = query.reshape(1,13)
        st.success(classify(model.predict(query)[0]))
prediction()


html_temp1 = """
<div style = "background-color: #70d4bc">
<p style = "color: white; text-align: center;">Designed & Developed By: <b>Rajashri Deka</b></p>
</div>
"""
st.markdown(html_temp1, unsafe_allow_html=True)
import streamlit as st
import pickle
import pandas as pd
import os
import numpy as np
import altair as alt
import time

model = pickle.load(open('model_prediksi_asuransi.sav', 'rb'))

@st.cache_data()
def get_fvalue(val):    
    feature_dict = {"Male":1,"Female":0}    
    for key,value in feature_dict.items():        
        if val == key:            
            return value
def get_svalue(val):    
    feature_dict = {"Yes":1,"No":0}    
    for key,value in feature_dict.items():        
        if val == key:            
            return value
def get_rvalue(val):    
    feature_dict = {"Southwest":1,"Northwest":2,"Southeast":3,"northeast":4}    
    for key,value in feature_dict.items():        
        if val == key:            
            return value
        
def get_value(val,my_dict):    
    for key,value in my_dict.items():        
        if val == key:            
            return value
        
app_mode = st.sidebar.selectbox('Select Page',['Home'])
if app_mode=='Home':
    st.title('CAR DATASET')
    # st.image('mobil.jpg')
    st.header('Dataset: ')
    data = pd.read_csv('insurance.csv')
    st.write(data)
    age = st.number_input('Input Your Age', 0,100)
    sex = st.radio('Set Your Gender', ['Male','Female'])
    bmi = st.number_input('Set Your BMI', 20,50)
    child = st.number_input('Input Your Children Count', 0, 10)
    smoker = st.radio('Are You A Smoker', ['Yes','No'])
    region = st.radio('Select Your Region', ['South','North','West','East'])
    if st.button('Prediksi'):
        charges_pred = model.predict([[age, get_fvalue(sex), bmi, child, get_svalue(smoker), get_rvalue(region)]])
        charges_str = np.array(charges_pred)
        charges_float = float(charges_str[0])

        charges_formated = "{:.2f}".format(charges_float)
        bar = st.progress(100)
        for percent_complete in range(100):
            time.sleep(0.01)
            bar.progress(percent_complete + 1)
        time.sleep(1)
        st.write("HASIL PREDIKSI BIAYA ASURANSI: $",charges_formated)
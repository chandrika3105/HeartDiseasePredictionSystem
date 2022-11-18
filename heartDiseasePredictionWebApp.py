# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:12:00 2022

@author: GAYATHRI
"""

import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('F:/Minor Project/trained_model.sav', 'rb'))

#creating a function for prediction

def heartdiseasepredict(input_data):

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data,dtype=float)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'The Person does not have a Heart Disease'
    else:
      return 'The Person has Heart Disease'
    
    
    
    
def main():
    
    #Giving a Title
    st.title('Heart Disease Prediction Web App')
    
    #getting input data
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    
    Age = st.text_input('Age')
    Sex = st.text_input('Sex')
    Cp = st.text_input('CP of heart')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Cholestrol')
    fbs = st.text_input('Fasting Blood Sugar')
    restecg = st.text_input('Resting Cardiographic')
    thalach = st.text_input('Maximum Heart Rate Achieved')
    exang = st.text_input('Exercise induced angina')
    oldpeak = st.text_input('Old Peak')
    slope = st.text_input('Slope')
    ca = st.text_input('Calcium present')
    thal = st.text_input('Thalassemia')
    
    
    #code for prediction
    
    heartDisease = ''
    
    #creating a button for prediction
    
    if st.button('HeartDisease Test Result'):
        heartDisease = heartdiseasepredict([Age,Sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
    
    st.success(heartDisease)
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
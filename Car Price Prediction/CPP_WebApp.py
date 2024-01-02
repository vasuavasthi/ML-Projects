# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 14:41:47 2023

@author: awast
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved mode
loaded_model=pickle.load(open('Car Price Prediction/CPP_trained_model.sav','rb')) 

#creating function for prediction
def Car_price_predictor(input_data):
    input_arr=np.array(input_data,dtype=np.float64)
    input_arr_r=input_arr.reshape(1,-1)
    pred=loaded_model.predict(input_arr_r)
    return pred
    
def main():
    
    #Giving title
    st.title('Car Price Prediction Web App')
    
    #Getting user input
    
    Year=st.text_input('Car Purchased Year')
    Present_Price=st.text_input('Car Present Price in lac\'s')
    Kms_Driven=st.text_input('Car has completed kms')
    F=st.selectbox('Type of fuel',['','Petrol','Diesel','CNG'])
    F=F.lower()
    Fuel_Type=10
    if F=='petrol':
        Fuel_Type=0
    elif F=='diesel':
        Fuel_Type=1
    elif F=='CNG':
        Fuel_Type=2   
    s=st.selectbox('Type of Seller',['','Dealer','Individual'])
    s=s.lower()
    seller_type=10
    if s=='dealer':
        seller_type=0
    elif s=='individual':
        seller_type=1    
    t=st.selectbox('Type of car transmission',['','Automatic','Manual'])
    t=t.lower()
    Transmission=10
    if t=='manual':
        Transmission=0
    elif t=='automatic':
        Transmission=1
    O=st.selectbox('Car has Owner or not',['','Yes','No'])
    O=O.lower()
    Owner=2
    if O=='yes':
        Owner=1
    elif O=='no':
        Owner=0
        
    predict=''
    
    if st.button("Predict Price"):
        predict=Car_price_predictor([Year,Present_Price,Kms_Driven,Fuel_Type,seller_type,Transmission,Owner])
        
    
    st.success(predict)
    
    
    
    
    
if __name__ == '__main__':
    main()










    

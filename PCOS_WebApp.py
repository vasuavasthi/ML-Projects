# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 14:41:47 2023

@author: awast
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved mode
loaded_model=pickle.load(open('PCOS_trained_model.sav','rb')) 

#creating function for prediction
def Pcos_detection(input_data):
    input_arr=np.array(input_data,dtype=np.float64)
    input_arr_r=input_arr.reshape(1,-1)
    pred=loaded_model.predict(input_arr_r)
    if pred[0]==0 :
       return 'PCOS Not Detected'
    else :
       return 'PCOS Detected' 
    
def main():
    
    #Giving title
    st.title('PCOS Detection System')
    
    
    fr=st.text_input('Right Follicle Number')
    fl=st.text_input('Left Follicle Number')
    s=st.selectbox('Skin Darkening',['','Yes','No'])
    s=s.lower()
    sd=2
    if s=='yes':
        sd=1
    elif s=='no':
        sd=0
    h=st.selectbox('Hair Growth',['','Yes','No'])
    h=h.lower()
    hg=2
    if h=='yes':
        hg=1
    elif h=='no':
        hg=0
    w=st.selectbox('Weight Gain',['','Yes','No'])
    w=w.lower()
    wg=2
    if w=='yes':
        wg=1
    elif w=='no':
        wg=0
    c=st.selectbox('Cycle',['','Regular','Irregular'])
    c=c.lower()
    cy=0
    if c=='regular':
       cy=2
    elif c=='irregular':
       cy=0
        
    predict=''
    
    if st.button("Detect"):
        predict=Pcos_detection([fr,fl,sd,hg,wg,cy])
        
    
    st.success(predict)
    
    
    
    
    
if __name__ == '__main__':
    main()










    

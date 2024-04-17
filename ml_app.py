import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.tree import DecisionTreeClassifier

#Loading up the classification model we created

model = DecisionTreeClassifier(max_depth=20, min_samples_leaf=5, random_state=0)

model = joblib.load('finalized_model.joblib')

@st.cache
def prediction(Buying,Maint,Doors,Persons,Lug_boots,Safety):
  if Safety == 'med':
    safety = 1
  elif Safety == 'high':
    safety = 2
  elif Safety == 'low':
    safety = 3
  df = pd.DataFrame([[Buying,Maint,Doors,Persons,Lug_boots,safety]],
                    columns=['Buying','Maint','Doors','Persons','Lug_boots','safety'])
  result=model.predict([[Buying,Maint,Doors,Persons,Lug_boots,safety]])
  return result


st.title('Car Evaluation Classification')
st.image("""https://media.zigcdn.com/media/model/2020/Jun/aspire_360x240.jpg""")
st.header('Enter the Information of the Car:')
st.text("vhigh=1 high=2 mid=3 low=4")
Buying = st.number_input('buying:', min_value=1, max_value=4, value=1)
st.text("vhigh = 1 high = 2 med 3 low = 4")
Maint = st.number_input('maint:', min_value=1, max_value=4, value=1)
st.text("2-Doors = 1 3-Doors 2 4-Doors = 3 5more = 4")
Doors = st.number_input('doors:', min_value=1, max_value=4, value=1)
st.text("2-persons = 1 4-persons = 2 more = 3 ")
Persons = st.number_input('persons:', min_value=1, max_value=3, value=1)
st.text("small 1 med 2 big = 3")
Lug_boot = st.number_input('lug_boot:', min_value=1, max_value=3, value=1)
Safty = st.radio('safty:', ('med', 'high', 'low'))

if st.button('Submit_Car_Infos'):
  cal_eval = prediction(Buying, Maint, Doors, Persons, Lug_boot, Safty)
  st.sucess(f,'The Evaluation of Car: {cal_eval[0]}')







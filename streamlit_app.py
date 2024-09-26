import streamlit as st
import pandas as pd

st.title('📈 Linear Regression App')

st.info('Hey, Welcome!!!')

st.write('This is a linear regression app that deploys the regression model for your data based on your inputs, please upload your data to proceed:')

st.text("") #add-line
col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1]) #splitting the space into 5 columns for alignment
st.markdown("***")
file = col3.file_uploader('Upload your CSV file', type="csv")

if(file):
  df = pd.read_csv(file)
  st.write('The uploaded file:')
  df





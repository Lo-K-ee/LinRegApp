import streamlit as st
import pandas as pd

st.title('📈 Linear Regression App')

st.info('Hey, Welcome!!!')

st.write('This is a linear regression app that deploys the regression model for your data based on your inputs, please upload your data to proceed:')

st.text("") #add-line
col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1]) #splitting the space into 5 columns for alignment
st.markdown("***")
file = col3.file_uploader('Upload your CSV file', type="csv")
df = None

with st.expander('Uploaded raw data'):
  if file is None:
    st.write('Please upload the file to continue')
  else:
    df = pd.read_csv(file)
    st.write('The file has been successfully uploaded:')
    df
    with st.expander('Select the variables for further analysis'):
      col_name = df.columns.to_list()
      # st.write('Choose the dependant variables:')
      st.radio('Choose the dependant variables:', col_name)





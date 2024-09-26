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
X = None
y = None

with st.expander('Uploaded raw data'):
  if file is None:
    st.write('Please upload the file to continue')
  else:
    df = pd.read_csv(file)
    st.write('The file has been successfully uploaded:')
    df
if df is not None:
  with st.expander('Select the variables for further analysis'):
    col_name = df.columns.to_list()
    dependent = st.multiselect('Choose the dependent variables:', col_name)
    independent = [item for item in col_name if item not in dependent]
    st.write('The dependent features are')
    dependent
    st.write('The independent features are')
    independent
    if st.button('Submit the features'):
      dep_features = dependent
      indep_features = independent
      dep_features
    
  # with st.expander('The variables for analysis are:')
  #   X = df.





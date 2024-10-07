import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


st.title('📈 Linear Regression App')

st.info('Hey, Welcome!!!')

st.write('This is a linear regression app that deploys the regression model for your data based on your inputs, please upload your data to proceed (*make sure to remove the columns with least importance for the analysis*) :')

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
  with st.expander('Normalizing the non-numerical features'):
    nonum_col = df.select_dtypes(exclude='number')
    nonum_col
    # if df.select_dtypes(exclude='number').shape[1] > 0:
    
if df is not None:
  with st.expander('Select the variables for further analysis'):
    col_name = df.columns.to_list()
    dependent = st.multiselect('Choose the dependent variables:', col_name)
    independent = [item for item in col_name if item not in dependent]
    st.write('The dependent columns are')
    dependent
    st.write('The independent columns are')
    independent
    if st.button('Submit the features'):
      dep_features = dependent
      indep_features = independent
      X = df[indep_features]
      y = df[dep_features]

if df is not None:
  with st.expander('The variables for analysis are:'):
    st.write('The dependent features')
    X
    st.write('The independent features')
    y

    



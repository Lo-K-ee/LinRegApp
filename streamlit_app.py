import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler


st.title('📈 Linear Regression App')

st.info('Hey, Welcome!!!')

st.write('This is a linear regression app that deploys the regression model for your data based on your inputs, please upload your data to proceed (*make sure to remove the least significant columns before uploading*) :')

st.text("") #add-line
col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1]) #splitting the space into 5 columns for alignment
st.markdown("***")
file = col3.file_uploader('Upload your CSV file', type="csv")
df = None # data 
X = None # independent features
y = None # dependent features
inc = 0 # incrementer

with st.expander('Uploaded raw data'):
  if file is None:
    st.write('Please upload the file to continue')
  else:
    df = pd.read_csv(file)
    st.write('The file has been successfully uploaded:')
    df
    
if df is not None:
  with st.expander('Normalizing the non-numerical features'):
    num_col = df.select_dtypes(include='number')
    nonum_col = df.select_dtypes(exclude='number')
    st.write('The non-numerical features are:')
    nonum_col
    if nonum_col.shape[1] > 0:
      norm_type = st.radio("Choose your Normalization method", ["Label Encoder", "One-Hot Encoder"], captions=["suitable for ordinal variables, where the categories have a specific order or ranking", 
                                                                                                   "suitable for situations where data has no relation to each other (ensure not to populate sparse features)"], index=None)
      if norm_type == "Label Encoder":
        le = LabelEncoder()
        for col in nonum_col.columns:
          df[col] = le.fit_transform(df[col])
        st.write('After encoding the features using label encoder')
        df
        inc += 1
      elif norm_type == "One-Hot Encoder":
        ohe = OneHotEncoder(sparse_output=False)
        encoded_cols = ohe.fit_transform(nonum_col)
        encoded_df = pd.DataFrame(encoded_cols, columns=ohe.get_feature_names_out(nonum_col.columns))
        df = pd.concat([df.drop(nonum_col.columns, axis=1), encoded_df], axis=1)
        st.write('After encoding the features using one-hot encoder')
        df
        inc += 1
                                

if inc == 1:
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
        inc += 1

if inc == 2:
  if df is not None:
    with st.expander('The variables for analysis are:'):
      st.write('The dependent features')
      y
      st.write('The independent features')
      X

if inc == 2:
  if df is not None:
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    with st.expander('Fitting the model & predicting:'):
      st.write('The model has been fitted to 80% training data and tested on the remaining 20% data')
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
      lin_reg = LinearRegression()
      lin_reg.fit(X_train, y_train)
      y_pred = lin_reg.predict(X_test)
      # Model Evaluation
      rmse = mean_squared_error(y_test, y_pred, squared=False)
      st.write(f'RMSE: {rmse}')
    
    



import streamlit as st

st.title('📈 Linear Regression App')

st.info('Hey, Welcome!!!')

st.write('This is a linear regression app that deploys the regression model for your data based on your inputs, please upload your data to proceed:')


col1, col2, col3 = st.columns([1,1,1])
st.markdown("***")
col2.button('upload')




import streamlit as st
import pandas as pd
import seaborn as sns

#this is a comment

st.title("Hello class")


add_selectbox = st.sidebar.radio(
    "How would you like to be contacted?",
    ("Sales", "Finance", "HR"))

if add_selectbox=='Sales':
    st.markdown ('''Welcome to *Sales*''')
elif add_selectbox == 'HR':
    st.markdown('''Hi_this_is_*HR*''')

else: 
    st.markdown('''Heloooo''')
    
 
[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

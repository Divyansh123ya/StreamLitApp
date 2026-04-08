import streamlit as st
import pandas as pd
st.header('Profile')
col1,col2 = st.columns([1,3])
with col1:
    st.image('4712293.png',width=150)
with col2:
    st.write('Name: Divyansh Rajpoot')
    st.write('Email: divyansh123ya@gmail.com')
st.divider
data = {
    "Level": ["10th", "12th", "Graduation 1st year","Graduation 2nd year"],
    "Board/University": ["CBSE", "CBSE", "ABES Engineering College","ABES Engineering College"],
    "Year": ["2021", "2023", "2024","2025"],
    "CGPA": ["80.66%", "84.2%", "7.95","8.0"]
}

df = pd.DataFrame(data)
st.table(df)

import streamlit as st
st.header('Profile')
col1,col2 = st.columns([1,3])
with col1:
    st.image('4712293.png',width=150)
with col2:
    st.write('Name: Divyansh Rajpoot')
    st.write('Email: divyansh123ya@gmail.com')
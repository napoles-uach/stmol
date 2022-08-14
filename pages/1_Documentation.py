import streamlit as st

st.title("Functions")
with open(f'functions.md', 'r') as f:           
    st.markdown(f.read())
import streamlit as st
from stmol import *

with open(f'README.md', 'r') as f:           
    st.markdown(f.read(),unsafe_allow_html=True)

import streamlit as st
from stmol import *

st.set_page_config(page_title="Stmol", page_icon="🧬",layout="wide")
st.sidebar.markdown('''
    [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&color=black&label)](https://github.com/napoles-uach/stmol)
    ''')  
with open(f'README.md', 'r') as f:           
    st.markdown(f.read(),unsafe_allow_html=True)

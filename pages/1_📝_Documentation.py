import streamlit as st

st.sidebar.markdown('''
    [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&color=black&label)](https://github.com/napoles-uach/stmol/blob/master/functions.md)
    ''')   
st.title("Functions")
with open(f'functions.md', 'r') as f:           
    st.markdown(f.read())

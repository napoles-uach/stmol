import streamlit as st
from stmol import showmol,obj_upload
import py3Dmol
uploaded_file = st.sidebar.file_uploader("Upload PDB file")
obj = obj_upload(uploaded_file)
showmol(obj,width=800)

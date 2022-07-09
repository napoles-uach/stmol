# Importing the installed libraries
    
import streamlit as st
from stmol import showmol
import py3Dmol
    
# Using Streamlit Syntax to build the Streamlit Widgets
    
st.sidebar.title('Demo app')
style = st.sidebar.selectbox('style',['cartoon','stick','sphere'])
    
# Creating the mol object using py3Dmol 
xyzview = py3Dmol.view(query='pdb:1A2C')
xyzview.setStyle({style:{'color':'spectrum'}})
xyzview.setBackgroundColor('white')
    
# Using the showmol function 
# from the stmol library to render the protein
showmol(xyzview, height = 500,width=800)

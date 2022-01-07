# streamlit_3dmol
This project aims to provide an easy way to create a web app for interacting with molecular structures using Streamlit. 


## Installation

```python
pip install stmol
```

## Example

```python
import streamlit as st
from stmol import showmol
import py3Dmol
st.sidebar.title('Show Proteins')
prot_str='1A2C,1BML,1D5M,1D5X,1D5Z,1D6E,1DEE,1E9F,1FC2,1FCC,1G4U,1GZS,1HE1,1HEZ,1HQR,1HXY,1IBX,1JBU,1JWM,1JWS'
prot_list=prot_str.split(',')
bcolor = st.sidebar.color_picker('Pick A Color', '#00f900')
protein=st.sidebar.selectbox('select protein',prot_list)
style = st.sidebar.selectbox('style',['line','cross','stick','sphere','cartoon','clicksphere'])
xyzview = py3Dmol.view(query='pdb:'+protein)
xyzview.setStyle({style:{'color':'spectrum'}})
xyzview.setBackgroundColor(bcolor)
showmol(xyzview, height = 500,width=800)
```



![gif](https://github.com/napoles-uach/streamlit_3dmol/blob/master/BRQqqfZ2lU.gif)

## Acknowledgment
If this software is useful in your work, please consider citing this repo:
<p>
https://github.com/napoles-uach/streamlit_3dmol
<p>
Thanks to the authors of 3Dmol.js : Nicholas Rego and David Koes.


# streamlit_3dmol
This project aims to provide an easy way to create a web app for interacting with molecular structures using Streamlit. 
Currently sub0.py is simply a static component call to 3Dmol.js by means of  component.html(), but the implementation of a bi-directional component seems to be straightforward.

## Installation

```python
pip install stmol
```

## Example

```python
import streamlit as st
from stmol import component_3dmol

st.title('Hello 3dmol component!!')
component_3dmol()
```



![GitHub Logo](https://github.com/napoles-uach/figuras/blob/master/stmol_image.png)


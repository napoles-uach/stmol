# streamlit_3dmol
This project aims to provide an easy way to create a web app for interacting with molecular structures using Streamlit. 
Currently sub0.py is simply a static component call to 3Dmol.js by means of  component.html(), but the implementation of a bi-directional component seems to be straightforward. Or you can install the whole project using pip as follows!!

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

## Acknowledgment
If this software is useful in your work, please consider citing this repo:

and use the following citation:

Nicholas Rego and David Koes
3Dmol.js: molecular visualization with WebGL
Bioinformatics (2015) 31 (8): 1322-1324 doi:10.1093/bioinformatics/btu829



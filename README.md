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
<p>
https://github.com/napoles-uach/streamlit_3dmol
<p>
and use the following citation:

Nicholas Rego and David Koes
3Dmol.js: molecular visualization with WebGL
Bioinformatics (2015) 31 (8): 1322-1324 doi:10.1093/bioinformatics/btu829

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">🧬 Want to interact with 3d molecular structures in your Streamlit app? Check out the community driven 3dmol Component that was just added to the gallery! <br><br>Thanks <a href="https://twitter.com/napoles3D?ref_src=twsrc%5Etfw">@napoles3D</a> for building it ❤️<br><br>🖥️ Repo: <a href="https://t.co/l8Yv3Q8nOz">https://t.co/l8Yv3Q8nOz</a><br>🎈 Gallery: <a href="https://t.co/ku0wJWDuhh">https://t.co/ku0wJWDuhh</a><a href="https://twitter.com/hashtag/microbiology?src=hash&amp;ref_src=twsrc%5Etfw">#microbiology</a> <a href="https://t.co/4JGaBoBEYL">pic.twitter.com/4JGaBoBEYL</a></p>&mdash; streamlit (@streamlit) <a href="https://twitter.com/streamlit/status/1294312584967987202?ref_src=twsrc%5Etfw">August 14, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

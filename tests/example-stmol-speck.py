import streamlit as st
#from stmol import speck_plot
from st_speckmol import spec_plot

st.markdown('''# speck_plot 
''')
st.sidebar.header("Add your own xyz coordinates below. :art:")
example_xyz = '''5
methane molecule (in ångströms)
C        0.000000        0.000000        0.000000
H        0.000000        0.000000        1.089000
H        1.026719        0.000000       -0.363000
H       -0.513360       -0.889165       -0.363000
H       -0.513360        0.889165       -0.363000
'''
_xyz = st.sidebar.text_area(
                label = "Paste your coordinates ⬇️",
                value = example_xyz, height  = 200)

st.code(_xyz.splitlines()[1])
res = spec_plot(_xyz,wbox_height="500px", wbox_width="500px")
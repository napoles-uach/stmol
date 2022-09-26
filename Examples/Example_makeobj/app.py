import streamlit as st
from stmol import showmol,makeobj
import py3Dmol
coords='''5
xyz coordinates of methane
C      0.00000    0.00000    0.00000
H      0.00000    0.00000    1.08900
H      1.02672    0.00000   -0.36300
H     -0.51336   -0.88916   -0.36300
H     -0.51336    0.88916   -0.36300
'''
obj=makeobj(coords,'xyz',style='sphere')
showmol(obj)

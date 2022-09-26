import streamlit as st
from stmol import showmol,render_pdb
import py3Dmol
obj=render_pdb(id='8DEP')
showmol(obj)

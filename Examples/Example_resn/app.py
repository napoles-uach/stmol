import streamlit as st
from stmol import showmol,render_pdb,render_pdb_resn
import py3Dmol
obj = render_pdb(id = '1A2C')
obj = render_pdb_resn(obj ,resn_lst = ['ALA',])
showmol(obj)

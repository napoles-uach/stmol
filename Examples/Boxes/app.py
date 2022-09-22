import streamlit as st
from stmol import py3Dmol, showmol,add_box
import py3Dmol
scene = py3Dmol.view(width=800,height=800)
add_box(scene)
add_box(scene,bxc=[5,5,5],boxColor='#CD5C5C',boxOpacity=1.0)
scene.zoom(0.2)
showmol(scene,width=800,height=800)

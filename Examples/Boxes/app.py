import streamlit as st
from stmol import showmol,add_box
import py3Dmol
scene = py3Dmol.view(width=800,height=800) # create the py3Dmol object (empty)
add_box(scene) # adds a box to the scene object with default values
add_box(scene,bxc=[5,5,5],boxColor='#CD5C5C',boxOpacity=1.0) # add a box with custom values
scene.zoom(0.2) # zoom
showmol(scene,width=800,height=800) #This renders the scene in the app

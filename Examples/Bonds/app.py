import streamlit as st
from stmol import showmol,add_sphere, add_cylinder
import py3Dmol
#In this example, we build a molecule like structure using the add_cylinder and add_sphere functions.

scene=py3Dmol.view(width=800,height=800) # Create a scene by defining a blank view

add_cylinder(scene,start=[0,0,0],end=[0,10,0],cylradius=0.5,cylColor='blue',dashed=False) # Add a cylinder (bond)
add_cylinder(scene,start=[0,0,0],end=[10,0,0],cylradius=0.5,cylColor='green',dashed=True) # Add a cylinder (dashed bond)

#add spheres at the end of the cylinders
add_sphere(scene,spcenter=[0,0,0],radius=2,spColor='red')
add_sphere(scene,spcenter=[0,10,0],radius=2,spColor='red')
add_sphere(scene,spcenter=[10,0,0],radius=3,spColor='purple')
scene.zoom(0.3) # Zoom in on the scene to have a nice view
showmol(scene,width=800,height=800) # This shows the scene in the streamlit web app

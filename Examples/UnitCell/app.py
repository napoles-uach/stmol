import streamlit as st
from stmol import showmol,add_box, add_sphere
import py3Dmol
#In this example, we build a unit cell like structure using the add_box and add_sphere functions.

scene=py3Dmol.view(width=800,height=800) # Create a scene by defining a blank view

add_box(scene,bxd=[10,10,10],bxc=[0,0,0],boxColor='blue',boxOpacity=0.7) # Add a box to the scene
#The box has length of 10 Angstroms in each direction, and is centered at the origin. It is blue and semi-transparent.

#Next, we will create a collection of spheres in each corner of the box.
#Each sphere will have a radius of 2 Angstroms, and will be colored red.
add_sphere(scene,spcenter=[5,5,5],radius=2,spColor='red')
add_sphere(scene,spcenter=[-5,5,5],radius=2,spColor='red')
add_sphere(scene,spcenter=[5,-5,5],radius=2,spColor='red')
add_sphere(scene,spcenter=[5,5,-5],radius=2,spColor='red')
add_sphere(scene,spcenter=[-5,-5,5],radius=2,spColor='red')
add_sphere(scene,spcenter=[5,-5,-5],radius=2,spColor='red')
add_sphere(scene,spcenter=[-5,5,-5],radius=2,spColor='red')
add_sphere(scene,spcenter=[-5,-5,-5],radius=2,spColor='red')

scene.zoom(0.3) # Zoom in on the scene to have a nice view
showmol(scene,width=800,height=800) # This shows the scene in the streamlit web app

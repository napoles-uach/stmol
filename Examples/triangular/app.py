import streamlit as st
from stmol import showmol,add_box
import py3Dmol
#In this example, we will explore how to work with the add_box function to create boxes.
#For this a colection of boxes is created in a double for loop. Because why not?

scene=py3Dmol.view(width=800,height=800) # Create a scene by defining a blank view
# In the following for loops, we create many boxes of different colors
for i in range(20):
    ii=i*10
    for j in range(10):
        jj=j*10
        if jj>ii: # This is to build boxes only for diagonal and above
            add_box(scene,bxc=[ii,jj,0],bxd=[10,10,10],boxColor=ii*693870+jj*10,boxOpacity=1.0)
scene.zoomTo() # This makes the scene zoom to the boxes
showmol(scene,width=800,height=800) # This shows the scene in the streamlit web app

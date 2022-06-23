import streamlit as st
import streamlit.components.v1 as components


body =  """
    <script src="https://cdn.jsdelivr.net/gh/arose/ngl@v0.10.4-1/dist/ngl.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function () {
      var stage = new NGL.Stage("viewport");
      stage.loadFile("rcsb://1crn", {defaultRepresentation: true});
    });
  </script>
  <div id="viewport" style="width:400px; height:300px;"></div>
    """

def func():
    return components.html(
        body
   ,
    height=600,
)

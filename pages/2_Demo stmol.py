
### Step 1) Imports

import streamlit as st
import py3Dmol
from stmol import showmol

### Step 2) Streamlit

st.sidebar.title("View Settings")

pdb_code = st.sidebar.text_input(
        label="PDB Code",
        value="3K8Y",
    )

hl_resi_list = st.sidebar.multiselect(label="Highlight Residues",options=list(range(1,5000)))

hl_chain = st.sidebar.text_input(label="Highlight Chain",value="A")

label_resi = st.sidebar.checkbox(label="Label Residues", value=True)

surf_transp = st.sidebar.slider("Surface Transparency", min_value=0.0, max_value=1.0, value=0.0)

hl_color = st.sidebar.text_input(label="Highlight Color",value="red")

bb_color = st.sidebar.text_input(label="Backbone Color",value="lightgrey")
lig_color = st.sidebar.text_input(label="Ligand Color",value="white")

st.markdown(f"## Stmol-App: PDB [{pdb_code.upper()}](https://www.rcsb.org/structure/{pdb_code}) (Chain {hl_chain})")

### Step 3) Py3Dmol

width = 700
height = 700

cartoon_radius = 0.2
stick_radius = 0.2

view = py3Dmol.view(query=f"pdb:{pdb_code.lower()}", width=width, height=height)

view.setStyle({"cartoon": {"style": "oval","color": bb_color,"thickness": cartoon_radius}})

view.addSurface(py3Dmol.VDW, {"opacity": surf_transp, "color": bb_color},{"hetflag": False})

view.addStyle({"elem": "C", "hetflag": True},
                {"stick": {"color": lig_color, "radius": stick_radius}})

view.addStyle({"hetflag": True},
                    {"stick": {"radius": stick_radius}})

for hl_resi in hl_resi_list:
    view.addStyle({"chain": hl_chain, "resi": hl_resi, "elem": "C"},
                    {"stick": {"color": hl_color, "radius": stick_radius}})

    view.addStyle({"chain": hl_chain, "resi": hl_resi},
                        {"stick": {"radius": stick_radius}})

if label_resi:
    for hl_resi in hl_resi_list:
        view.addResLabels({"chain": hl_chain,"resi": hl_resi},
        {"backgroundColor": "lightgray","fontColor": "black","backgroundOpacity": 0.5})

### Step 4) Stmol

showmol(view, height=height, width=width)
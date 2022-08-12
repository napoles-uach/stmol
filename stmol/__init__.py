import os
import streamlit.components.v1 as components
import ipywidgets as widgets
from ipywidgets import embed
import py3Dmol
import ipyspeck

def showmol(mol_obj,height=500,width=500):
    """Shows the Py3DMOL object.

    Parameters
    ----------
    obj: Py3DMOL object
        Already existing Py3DMOL object, which can be created using the makeobj function.
    height: Integer, default 500
        Is the height of viwer window.
    width: Integer, default 500
        Is the width of wiewer window.
    
    Returns
    -------
    None.
    """
    components.html(mol_obj._make_html(), height = height,width=width)

def speck_plot(_xyz, wbox_height="700px", 
            wbox_width="800px",
            component_h = 700, 
            component_w = 800, 
            scroll = False):

    """ Plots the speckmol molecule using the ipyspeck library and returns 
        the <class 'ipyspeck.speck.Speck'>.
    
    Parameters
    ----------
    _xyz : str
        The xyz string of the molecule.
    wbox_height : str
        The height of the widget box.
    wbox_width : str
        The width of the widget box.
    component_h : int
        The height of the streamlit html component.
    component_w : int
        The width of the streamlit html component.
    scroll : bool
        If True, the streamlit component will scroll.  
    Returns
    -------
    spec_xyz : <class 'ipyspeck.speck.Speck'>
        The speckmol molecule. spec_xyz.keys() returns the keys of the
        molecule. For example - spec_xyz.keys() returns ['atomScale',  
        'bondScale', 'atomShade', 'bondThreshold', 'bondColor', 'atomColor',
        'outline', 'bonds', 'atomScale', 'atomColor', 'atomScale', 'atomScale]
        These keys are useful for modifying the molecule.
    """        
    # Read the xyz file
    spec_xyz = ipyspeck.speck.Speck(data = _xyz)
    # Create the widget box
    widg = widgets.Box([spec_xyz], layout=widgets.Layout(height=wbox_height,width=wbox_width))
    # Embed the widget box in the streamlit html component
    sc = embed.embed_snippet(widg)
    html = embed.html_template.format(title="", snippet=sc)
    components.html(html,height = component_h, width = component_w,scrolling=scroll)
    return spec_xyz

def makeobj(xyz,molformat='mol',style='stick',background='white'):
    """
    makeobj function accepts a molecule structure in a given format and returns a Py3DMOL molecule object.
    Accepted formats are 'mol', 'sdf', 'pdb', 'pqr', 'xyz'.

    Parameters
    ----------
    xyz: String
        Is the molecule object
    molformat: String, default 'mol'    
        Is the format of the molecule. Accepted formats are 'mol', 'sdf', 'pdb', 'pqr', 'xyz'.
    style: String, default 'stick'
        Is the style of the molecule. Can be 'stick', 'sphere', 'cross', 'surface', 'ribbon', 'cartoon'
    background: String, default 'white'
        Is the background color of the molecule
    
    Returns
    -------
    obj: Py3DMOL object
    """
    xyzview = py3Dmol.view()
    xyzview.addModel(xyz,molformat)
    xyzview.setStyle({style:{}})
    xyzview.setBackgroundColor(background)
    xyzview.zoomTo()
    return xyzview

def render_pdb(id='7T59'):
    """
    render_pdb function accepts a PDB ID and returns a Py3DMOL object.
    Example:
        obj=render_pdb()
        showmol(obj)

    Parameters
    ----------
    id: String, default '7T59'
        Is the PDB ID of the molecule.
    
    Returns
    -------
    obj: Py3DMOL object
    """
    viewer = py3Dmol.view(query=id)
    viewer.setStyle({ "cartoon": {
        "color": "spectrum",
        "colorReverse": True,
        "colorScale": "RdYlGn",
        "colorScheme": "Polarity",
        "colorBy": "resname",
            }})
    return viewer

def render_pdb_resn(viewer,resn_lst):
    """
    render_pdb_resn function accepts a Py3DMOL object and adds a list of PDB resn labels to it.
    Example:
        showmol(render_pdb_resn(render_pdb(),['ALA',]) )

    Parameters
    ----------
    viewer: Py3DMOL object
    resn_lst: List
        Is the list of PDB resn of the molecules. Example: ['ALA','ARG',,'LYS','THR','TRP','TYR','VAL']
    
    Returns
    -------
    obj: Py3DMOL object
    """
    viewer.setStyle({ "cartoon": {"color": "spectrum","colorBy": "resname",}})
    viewer.setStyle({'bonds':0},{'sphere':{'radius':0.3}})
    viewer.addResLabels({'resn':resn_lst,})
    return viewer

def render_pdb_resi(viewer,resi_lst):
    """
    render_pdb_resi function accepts a Py3DMOL object and adds a list of PDB resi labels to it.
    Example:
        showmol(render_pdb_resi(render_pdb(),['442-444']))

    Parameters
    ----------
    viewer: Py3DMOL object
    resi_lst: List
        Is the list of PDB resi of the molecules. Example: ['42-44','48','49']
    
    Returns
    -------
    obj: Py3DMOL object
    """
    viewer.setStyle({"cartoon": {"color": "spectrum","colorBy": "resname",}})
    viewer.setStyle({'bonds':0},{'sphere':{'radius':0.3}})
    viewer.addResLabels({'resi':resi_lst,})
    return viewer

def obj_upload(uploaded_file):
    """
    obj_upload function accepts a file uploaded with streamlit file_uploader function and returns a Py3DMOL object.
    Accepted formats are 'mol', 'sdf', 'pdb', 'pqr', 'xyz'.
    Example:
        uploaded_file = st.sidebar.file_uploader("Upload PDB file")
        if uploaded_file is not None:
            prot = obj_upload(uploaded_file)
            showmol(prot)

    Parameters
    ----------
    uploaded_file: File
        Is the PDB, xyz or any supported file of the molecule
    
    Returns
    -------
    obj: Py3DMOL object
    """
       
    pdbxyz = uploaded_file.getvalue().decode("utf-8")
    prot=makeobj(xyz=pdbxyz,molformat='pdb',style='stick',background='white')
    return prot

def add_model(obj,xyz,molformat='mol',model_style='stick'):
    """
    Adds a model to an existing Py3DMOL object.
    
    Parameters
    ----------
    obj: Py3DMOL object
        Already existing Py3DMOL object.
    xyz: String
        Is the model to be added.
    molformat: String, default 'mol'    
        Is the format of the added model
    model_style: String, default 'stick'
        Is the style of the added model. Can be 'stick', 'sphere', 'cross', 'surface', 'ribbon', 'cartoon'
    
    Returns
    -------
    None.
    """
    obj.addModel(xyz,molformat)
    obj.setStyle({'model':-1},{model_style:{}})

def add_hover(obj,backgroundColor='white',fontColor='black'):
    """
    Adds a hover function to the Py3DMOL object to show the atom name when the mouse hovers over an atom.
    Example:
        obj = render_pdb()
        add_hover(obj)
        showmol(obj)

    Parameters
    ----------
    obj: Py3DMOL object
        Already existing Py3DMOL object, which can be created using the makeobj function.
    backgroundColor: String, default 'white'
        Is the background color of the hover text
    fontColor: String, default 'black'
        Is the color of the text

    Returns
    -------
    None.
    """

    js_script = """function(atom,viewer) {
                   if(!atom.label) {
                    atom.label = viewer.addLabel(atom.atom+':'+atom.serial,{position: atom, backgroundColor:"%s" , fontColor:"%s"});
                }
              }"""%(backgroundColor,fontColor)
    obj.setHoverable({},True,js_script,
               """function(atom,viewer) {
                   if(atom.label) {
                    viewer.removeLabel(atom.label);
                    delete atom.label;
                   }
                }"""
               )

def add_box(obj,bxc=[0,0,0],bxd=[10,10,10],boxColor='blue',boxOpacity=0.5): 
    """
    Adds a box to an existing Py3DMOL object.
    Example:
        obj = render_pdb()
        add_box(obj)
        showmol(obj)

    Parameters
    ----------
    obj: Py3DMOL object 
        Already existing Py3DMOL object, which can be created using the makeobj function.
    bxc: List of Integers of len 3, default [0,0,0]
        Are the x,y,z coordinates of the center of the box in Angstroms
    bxd: List of Integers of len 3, default [10,10,10]
        Are the x,y,z dimensions of the box in Angstroms
    boxColor: String, default 'blue'
        Is the color of the box
    boxOpacity: String, default 0.5
        Is the opacity of the box
    
    Returns
    -------
    None.
    """
    obj.addBox({
        'center':{'x':bxc[0],'y':bxc[1],'z':bxc[2]},
        'dimensions': {'w':bxd[0],'h':bxd[1],'d':bxd[2]},
        'color':boxColor,
        'opacity': boxOpacity
        })

def add_sphere(obj,spcenter=[0,0,0],radius=10,spColor='blue'):
    """
    Adds a sphere to an existing Py3DMOL object.
    Example:
        obj = render_pdb()
        add_sphere(obj)
        showmol(obj)

    Parameters
    ----------
    obj: Py3DMOL object 
        Already existing Py3DMOL object, which can be created using the makeobj function.
    spcenter: List of Integers of len 3, default [0,0,0].
        Are the x,y,z coordinates of the center of the sphere in Angstroms
    radius: integer, default 10
        Is the radius of the sphere in Angstroms.
    spColor: String, default 'blue'
        Is the color of the sphere.
    
    Returns
    -------
    None.
    """
    obj.addSphere({
        'center':{'x':spcenter[0],'y':spcenter[1],'z':spcenter[2]},
        'radius':radius,
        'color':spColor
        })

def add_cylinder(obj,start=[0,0,0],end=[0,0,1],cylradius=1,cylColor='blue',dashed=True):
    """
    Adds a cylinder to an existing Py3DMOL object.
    Example:
        obj = render_pdb()
        add_cylinder(obj,end=[0,0,10])
        showmol(obj)

    Parameters
    ----------
    obj: Py3DMOL object
        Already existing Py3DMOL object, which can be created using the makeobj function.
    start: List of Integers of len 3, default [0,0,0]
        Are the x,y,z coordinates of the start of the cylinder in Angstroms.
    end: List of Integers of len 3, default [0,0,1]
        Are the x,y,z coordinates of the end of the cylinder in Angstroms.
    cylradius: integer, default 1
        Is the radius of the cylinder in Angstroms.
    cylColor: String, default 'blue'
        Is the color of the cylinder.
    dashed: Boolean, default True
        True for a cylinder dashed. False for a solid cylinder.
    
    Returns
    -------
    None.
    """

    obj.addCylinder({
        'start':{'x':start[0],'y':start[1],'z':start[2]},
        'end':{'x':end[0],'y':end[1],'z':end[2]},
        'radius':cylradius,
        'fromCap':True,
        'toCap':True,
        'color':cylColor,
        'dashed':dashed

        })

### showmol(obj,height=500,width=500)
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

#### speck_plot(_xyz, wbox_height="700px", wbox_width="800px",component_h = 700, component_w = 800, scroll = False)
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

### makeobj(xyz,molformat='mol',style='stick',background='white')
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
### render_pdb(id='7T59')
    """
    render_pdb function accepts a PDB ID and returns a Py3DMOL object.

    Parameters
    ----------
    id: String, default '7T59'
        Is the PDB ID of the molecule.
    
    Returns
    -------
    obj: Py3DMOL object
    """
### render_pdb_resn(viewer,resn_lst)
    """
    render_pdb_resn function accepts a Py3DMOL object and adds a list of PDB resn labels to it.

    Parameters
    ----------
    viewer: Py3DMOL object
    resn_lst: List
        Is the list of PDB resn of the molecules. Example: ['ALA','ARG',,'LYS','THR','TRP','TYR','VAL']
    
    Returns
    -------
    obj: Py3DMOL object
    """
### render_pdb_resi(viewer,resi_lst)
    """
    render_pdb_resi function accepts a Py3DMOL object and adds a list of PDB resi labels to it.

    Parameters
    ----------
    viewer: Py3DMOL object
    resi_lst: List
        Is the list of PDB resi of the molecules. Example: ['42-44','48','49']
    
    Returns
    -------
    obj: Py3DMOL object
    """
### obj_upload(uploaded_file)
    """
    obj_upload function accepts a file uploaded with streamlit file_uploader function and returns a Py3DMOL object.
    Accepted formats are 'mol', 'sdf', 'pdb', 'pqr', 'xyz'.
    In Streamlit a file can be uploaded with: 
        
        uploaded_file = st.sidebar.file_uploader("Upload PDB file")

    Parameters
    ----------
    uploaded_file: File
        Is the PDB, xyz or any supported file of the molecule
    
    Returns
    -------
    obj: Py3DMOL object
    """
### add_model(obj,xyz,molformat='mol',model_style='stick')
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
### add_hover(obj,backgroundColor='white',fontColor='black')
    """
    Adds a hover function to the Py3DMOL object to show the atom name when the mouse hovers over an atom.

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
### add_box(obj,bxc=[0,0,0],bxd=[10,10,10],boxColor='blue',boxOpacity=0.5)
    """Adds a box to an existing Py3DMOL object.

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
### add_sphere(obj,spcenter=[0,0,0],radius=10,spColor='blue')
    """Adds a sphere to an existing Py3DMOL object.

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
### add_cylinder(obj,start=[0,0,0],end=[0,0,1],cylradius=1,cylColor='blue')
    """Adds a cylinder to an existing Py3DMOL object.

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







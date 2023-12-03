# Stmol
[ ![](https://img.shields.io/badge/Paper-Frontiers-red) ](https://www.frontiersin.org/articles/10.3389/fmolb.2022.990846/full)\
A component for building interactive molecular visualizations within Streamlit web-applications. It is designed to provide a state of the art visualizing and rendering 3D molecular structures for researchers, in a user-friendly manner.

------------------------------
## Note: Due to recent changes in the 3Dmol.js package, it is recomended to install py3DMol in the following way,
```
pip install py3Dmol==2.0.0.post2
```
## Stmol features 

- An easy-to-use component for rendering interactive 3D molecular visualizations of protein and ligand structures within Streamlit web-apps
- `stmol` can render protein and ligand structures with just a few lines of Python code by utilizing popular visualization libraries, currently Py3DMol and Speck. 
- On the user-end, `stmol` does not require expertise to interactively navigate. 
- On the developer-end, `stmol` can be easily integrated within structural bioinformatic and cheminformatic pipelines to provide a simple means for user-end researchers to advance biological studies and drug discovery efforts.
------------------------------

## Stmol installation

`stmol` runs with traditional Python stack.
To install `stmol` from [pypi](https://pypi.org/project/stmol/), run this command in your terminal:

``` console
pip install stmol==0.0.9
```

Since the end goal of `stmol` plugin, is to enable easy rendering of molecular structure within the streamlit applicaton, libraries such as 
[streamlit](https://github.com/streamlit/streamlit) and [py3Dmol](https://pypi.org/project/py3Dmol/) are crucial to work with. 
Run this command in your terminal to install the latest release of Streamlit,
``` console
pip install streamlit
```
Run this command in your terminal to install the latest release of py3Dmol,
``` console
pip install py3Dmol
```
A recent addition to `stmol` project, in a form of static HTML wrapper is the `speck_plot()` function, which helps in rendering [Speck](https://github.com/wwwtyro/speck) structures within the Streamlit web-application, is dependent on the following libraries, 
```console
ipyspeck(==0.6.1)
ipywidgets(==7.6.3)
ipython_genutils
```

-----------------

## Quickstart

##### 1. Protein visualization using `showmol()`function 

- **Using `py3Dmol object`**

To visualize any protein structure, all we need is the PDB ID of the protein.
```python
from stmol import showmol
import py3Dmol
# 1A2C
# Structure of thrombin inhibited by AERUGINOSIN298-A from a BLUE-GREEN ALGA
xyzview = py3Dmol.view(query='pdb:1A2C') 
xyzview.setStyle({'cartoon':{'color':'spectrum'}})
showmol(xyzview, height = 500,width=800)
```
- **Using the `render_pdb()` function**

The `render_pdb()` function accepts any PDB ID and returns a py3Dmol object. 
```python
from stmol import *
showmol(render_pdb(id = '1A2C'))
```
[![Quickstart-1](https://github.com/napoles-uach/stmol/blob/master/Resources/Quickstart-1.gif)](https://github.com/napoles-uach/stmol/blob/master/Resources/Quickstart-1.gif)

##### 2. Labelling protein using `render_pdb_resn()`function 
Inorder to mark the residues, we can use the `render_pdb_resn()` function, which in this example marks the *Alanine* [ALA] residues,
```python
showmol(render_pdb_resn(viewer = render_pdb(id = '1A2C'),resn_lst = ['ALA',]))
```
[![Quickstart-2](https://github.com/napoles-uach/stmol/blob/master/Resources/Quickstart-2.png)](https://github.com/napoles-uach/stmol/blob/master/Resources/Quickstart-2.png)

###### Refer to the documentation [here](https://napoles-uach-stmol-home-pom051.streamlitapp.com/Documentation) 
----------
## Examples
You can find several `stmol` examples [here](https://napoles-uach-stmol-home-pom051.streamlitapp.com/Examples).

### Browser support
- Chrome, Edge, Firefox - [link](https://napoles-uach.github.io/stmol/)
- Safari - [link](https://napoles-uach-stmol-home-pom051.streamlitapp.com)

----------------
## Dependencies
- [py3Dmol](https://pypi.org/project/py3Dmol/) 
- [ipyspeck](https://pypi.org/project/ipyspeck/)
- [ipywidgets](https://github.com/jupyter-widgets/ipywidgets)
- [streamlit](https://github.com/streamlit/streamlit)
- [ipython_genutils](https://github.com/ipython/ipython_genutils)
-----------------

## Contribution to the project
We appreciate contributions from the community! Every little bit helps, and credit will always be given. 
- **Reporting Bugs** - Report bugs at https://github.com/napoles-uach/stmol/issues
- **Fix Bugs** - Look through the GitHub issues for bugs. Anything tagged with “bug” and “help wanted” is open to whoever wants to help with it.
- **Implement Features** - Look through the GitHub issues for features. Anything tagged with “enhancement” and “help wanted” is open to whoever wants to implement it.
- **Submit Feedback** - The best way to send feedback is to file an issue at https://github.com/napoles-uach/stmol/issues
--------------
## Authors
- J. M. Nápoles-Duarte <jnapoles@uach.mx>
- Avratanu Biswas <avratanu.biswas@brc.hu>
- Mitchell I. Parker <mip34@drexel.edu>

## Aknowledgments
We thank the authors of 3dmol.js and py3Dmol.
Nicholas Rego, David Koes, 3Dmol.js: molecular visualization with WebGL, Bioinformatics, Volume 31, Issue 8, 15 April 2015, Pages 1322–1324, https://doi.org/10.1093/bioinformatics/btu829

## How to cite
Please include this citation if Stmol is used in an academic study:

Nápoles-Duarte JM, Biswas A, Parker MI, Palomares-Baez JP, Chávez-Rojo MA and Rodríguez-Valdez LM (2022) Stmol: A component for building interactive molecular visualizations within streamlit web-applications. Front. Mol. Biosci. 9:990846. doi: 10.3389/fmolb.2022.990846

Or use the following bibtex format,
```
@ARTICLE{stmol,
  
AUTHOR={Nápoles-Duarte, J.M. and Biswas, Avratanu and Parker, Mitchell I. and Palomares-Baez, J.P. and Chávez-Rojo, M. A. and Rodríguez-Valdez, L. M.},   
	 
TITLE={Stmol: A component for building interactive molecular visualizations within streamlit web-applications},      
	
JOURNAL={Frontiers in Molecular Biosciences},      
	
VOLUME={9},           
	
YEAR={2022},      
	  
URL={https://www.frontiersin.org/articles/10.3389/fmolb.2022.990846},       
	
DOI={10.3389/fmolb.2022.990846},      
	
ISSN={2296-889X},   
}
```


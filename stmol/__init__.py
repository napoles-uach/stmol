import os
import streamlit.components.v1 as components

def showmol(mol_obj,height=500,width=500):
    components.html(mol_obj._make_html(), height = height,width=width)


def component_3dmol(width=800, height=800):
    """
    Renders a molecule component

    Parameters
    ----------
    width : int
        width of component
    
    height : int
        height of component
    """
    components.html('''
<head>
    <script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>

    <form enctype="multipart/form-data">
        <input id="ligand" type="file" />
    </form>

    <script>
        var glviewer = null;
        var labels = [];

        var colorSS = function (viewer) {
            //color by secondary structure
            var m = viewer.getModel();
            m.setColorByFunction({}, function (atom) {
                if (atom.ss == 'h') return "magenta";
                else if (atom.ss == 's') return "orange";
                else return "white";
            });
            viewer.render();
        }

        var atomcallback = function (atom, viewer) {
            if (atom.clickLabel === undefined
                || !atom.clickLabel instanceof $3Dmol.Label) {
                atom.clickLabel = viewer.addLabel(atom.elem + atom.serial, {
                    fontSize: 14,
                    position: {
                        x: atom.x,
                        y: atom.y,
                        z: atom.z
                    },
                    backgroundColor: "black"
                });
                atom.clicked = true;
            }

            //toggle label style
            else {

                if (atom.clicked) {
                    var newstyle = atom.clickLabel.getStyle();
                    newstyle.backgroundColor = 0x66ccff;

                    viewer.setLabelStyle(atom.clickLabel, newstyle);
                    atom.clicked = !atom.clicked;
                }
                else {
                    viewer.removeLabel(atom.clickLabel);
                    delete atom.clickLabel;
                    atom.clicked = false;
                }

            }
        };
        var readText = function (input, func) {
            if (input.files.length > 0) {
                var file = input.files[0];
                var reader = new FileReader();
                reader.onload = function (evt) {
                    func(evt.target.result, file.name);
                };
                reader.readAsText(file);
                $(input).val('');
            }
        };

        $(document).ready(function () {

            moldata = data = $("#ligand").val();
            glviewer = $3Dmol.createViewer("gldiv", {
                defaultcolors: $3Dmol.rasmolElementColors
            });
            glviewer.setBackgroundColor(0xffffff);

            receptorModel = m = glviewer.addModel(data, "pqr");

            atoms = m.selectedAtoms({});

            for (var i in atoms) {
                var atom = atoms[i];
                atom.clickable = true;
                atom.callback = atomcallback;
            }

            glviewer.mapAtomProperties($3Dmol.applyPartialCharges);
            glviewer.zoomTo();
            glviewer.render();
        });
    </script>
</head>

<body>

    <div id="gldiv" style="width: 100%; height: 40vh; margin: 0; padding: 0; border: 0;"></div>

    <hr style="margin: 0;">

    <br>
    Set structure Identifier (For example 6VXX) and click download:

    <input id="pdbid" value="6VXX" size=4>
    <button
        onclick="glviewer.clear(); m = $3Dmol.download('pdb:' + $('#pdbid').val(), glviewer, {doAssembly:true, noSecondaryStructure: false});">Download</button>

    <br>

    or upload local file <input type="file"
        onchange="readText(this, function(data, name) {glviewer.clear(); m= glviewer.addModel(data,name); glviewer.zoomTo(); glviewer.render();} );">
    <br>
    <hr>
    <br>
    <p style="font-size:22px;">Customize visualization:</p>

    For small molecules

    <input type="button" value="Stick" onclick="glviewer.setStyle({},{stick:{}}); glviewer.render();"></input>

    <input type="button" value="Sphere" onclick="glviewer.setStyle({},{sphere:{}}); glviewer.render();"></input>

    <br>

    Change box opacity

    <input type="range" min="0" max="100" value="50" class="slider" id="opacitySlider">
    <input type="button" value="Render box"
        onclick="glviewer.addBox({center:{x:200,y:180,z:160},dimensions: {w:60,h:60,d:80},color:'magenta',opacity: document.getElementById('opacitySlider').value / 100});glviewer.render();"></input>

    <br>

    For proteins

    <input type="button" value="Cartoon"
        onclick="glviewer.setStyle({hetflag:false},{cartoon:{}}); glviewer.render();"></input>

    <input type="button" value="Color SS" onclick="colorSS(glviewer);"></input>

</body>
''', width=width, height=height)
    return 

########### The part below is for making the component bidirectional
########### In may not interfere with the code above



# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "my_component",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("my_component", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def my_component(title,subtitle,body,link,color):
    """Create a new instance of "my_component".
 """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    _ = _component_func(
        title=title,subtitle=subtitle,body=body,link=link,color=color)
    
    




# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/__init__.py`
if not _RELEASE:
    import streamlit as st


    num_clicks = my_component("Title1","Subtitle","some random text","https://www.google.com","blue")
    




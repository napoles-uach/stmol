# Importing the installed libraries
import streamlit as st
from stmol import *
import py3Dmol
import glob  

st.sidebar.markdown('''
    [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&color=black&label)](https://github.com/napoles-uach/stmol/blob/master/pages/3_Examples.py)
    ''')  
tab1,tab2, tab3 = st.tabs(['Example-1 py3Dmol','Example-2 Speck', 'Example-3 stmol-extras'])

with tab1:  
    with st.echo(code_location='below') :
        # Code Block
        prot_str='1A2C,1BML,1D5M,1D5X,1D5Z,1D6E,1DEE,1E9F,1FC2,1FCC,1G4U,1GZS,1HE1,1HEZ,1HQR,1HXY,1IBX,1JBU,1JWM,1JWS'
        prot_list=prot_str.split(',')
        bcolor = st.color_picker('Pick A Color','#89cff0')
        protein=st.selectbox('select protein',prot_list)
        style = st.selectbox('style',['cartoon','line','cross','stick','sphere'])
        xyzview = py3Dmol.view(query='pdb:'+protein)
        xyzview.setStyle({style:{'color':'spectrum'}})
        xyzview.setBackgroundColor(bcolor)
        showmol(xyzview, height = 500,width=800)
        
        
with tab2:
    with st.echo(code_location='below') :
        # Code Block 
        options = st.radio(label = "",options=['Load xyz', 'Paste xyz'],horizontal=True)
        if options == 'Paste xyz':
            
            example_xyz = '''46
            testosterone
            C     -4.0599     -2.1760     -0.8224
            O     -4.9516     -2.8840     -1.2414
            C     -4.2163     -0.6676     -0.7586
            C     -2.8826      0.0343     -0.9993
            C     -2.7857     -2.7158     -0.3131
            C     -1.7443     -1.9501      0.0575
            C     -0.5249     -2.5861      0.6659
            C      0.7827     -1.9356      0.2082
            C      0.7295     -0.4182      0.4294
            C      2.0267      0.2733     -0.0072
            C      3.3706     -0.1900      0.5799
            C      4.3192      1.0027      0.3273
            C      3.4317      2.2202     -0.0268
            O      3.9384      3.3043      0.7679
            C      1.9714      1.7980      0.3340
            C      1.7106      2.0852      1.8182
            C      0.8686      2.4201     -0.5385
            C     -0.4798      1.7315     -0.2601
            C     -0.4282      0.1930     -0.4091
            C     -1.7900     -0.4363     -0.0132
            H     -2.7575     -3.8052     -0.2565
            H     -0.6135     -2.5201      1.7733
            H     -0.4925     -3.6738      0.4451
            H      1.6336     -2.3732      0.7646
            H      0.9690     -2.1675     -0.8583
            H      0.5479     -0.2168      1.5138
            H      2.1058      0.1678     -1.1210
            H      3.2853     -0.4094      1.6573
            H      3.7364     -1.1101      0.0994
            H      4.9267      1.2382      1.2217
            H      5.0342      0.7890     -0.4822
            H      3.5293      2.5237     -1.0880
            H      3.2906      4.0296      0.8195
            H      0.8832      1.4797      2.2078
            H      2.5972      1.8604      2.4268
            H      1.4613      3.1361      1.9910
            H      0.7818      3.5044     -0.3452
            H      1.1247      2.3262     -1.6107
            H     -0.8205      1.9959      0.7596
            H     -1.2411      2.1442     -0.9502
            H     -0.2361     -0.0466     -1.4843
            H     -4.6390     -0.3984      0.2304
            H     -4.9734     -0.3373     -1.4982
            H     -2.5493     -0.1544     -2.0405
            H     -3.0184      1.1303     -0.9178
            H     -2.0604     -0.0823      1.0166
            '''
            _xyz = st.text_area(
                            label = "Enter xyz coordinates below ⬇️",
                            value = example_xyz, height  = 200)

            st.success(_xyz.splitlines()[1],icon="✅")
            res = speck_plot(_xyz,wbox_height="500px", wbox_width="500px")
        else:
            ex_files = glob.glob("xyz_mol_examples/*.xyz")
            example_xyz = st.selectbox("Select a molecule",ex_files)
            f = open(example_xyz,"r")
            example_xyz = f.read()
            st.info(example_xyz.splitlines()[1], icon="✅")
            res = speck_plot(example_xyz,wbox_height="500px",wbox_width="500px")
            st.info("Example Source - https://github.com/wwwtyro/speck/tree/gh-pages/static/samples",icon="ℹ️")

    with tab3 :
        with st.echo():
            showmol(render_pdb_resn(viewer = render_pdb(id = '1A2C'),resn_lst = ['ALA',]),height=700,width=700)

        

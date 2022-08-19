import streamlit as st

st.sidebar.markdown('''
    [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&color=black&label)](https://github.com/napoles-uach/stmol/blob/master/pages/4_More%20Information.py)
    ''')  

st.markdown('''
            ## Authors
            - J. M. N  ́apoles-Duarte <jnapoles@uach.mx>
            - Avratanu Biswas <avratanu.biswas@brc.hu>
            - Mitchell I. Parker <mip34@drexel.edu>
            ''')
st.markdown(''' ---------------------------''')


with open(f'changelog.md', 'r') as f:           
    st.markdown(f.read())

st.markdown(''' ---------------------------''')    
st.markdown('''
            ## Resources
            - 3DmolJs - http://3dmol.csb.pitt.edu , https://pubmed.ncbi.nlm.nih.gov/25505090/
            - Speck - https://github.com/wwwtyro/speck , http://wwwtyro.github.io/speck/
            - Related blogs - https://towardsdatascience.com/molecular-visualization-in-streamlit-using-rdkit-and-py3dmol-part-2-657d28152753
        ''')
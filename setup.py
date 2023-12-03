import setuptools

setuptools.setup(
    name="stmol",
    version="0.0.7",
    author="Jose Manuel Napoles Duarte",
    author_email="jnapoles@uach.mx",
    description="Streamlit component for molecular visualization",
    long_description="stmol is based on popular visualization software 3Dmol.js",
    long_description_content_type="text/plain",
    url="https://github.com/napoles-uach/streamlit_3dmol",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
        "py3Dmol",
        "ipyspeck==0.6.1", 
        "ipywidgets==7.6.3"
        "ipython_genutils",
    ],
)

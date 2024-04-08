import streamlit as st
import geemap.foliumap as geemap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Please note that this page is under construction...
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Streamlit + Leafmap Web App")

st.markdown(
    """
    Welcome ! This multipage app serves as a sandbox to create a geospatial data reviewer.
    Its goal is to demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://book.leafmap.org/index.html).
    """
)

st.header("Instructions")

markdown = """
Have a look at the different pages on the sidebar!
"""

st.markdown(markdown)

m = geemap.Map()
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)

st.header("Ressources")
markdown = """
Work based on various ressources and documentation from Dr. Qiusheng Wu ([GitHub](https://github.com/giswqs)).
Leafmap on GitHub: https://github.com/opengeos/leafmap.
Streamlit + GEE Web App URL: <https://geemap.streamlit.app>. [GitHub repository](https://github.com/giswqs/geemap-apps).
Leafmap + Streamlit demo on GitHub: https://github.com/giswqs/leafmap-streamlit/tree/master.
"""

st.markdown(markdown)
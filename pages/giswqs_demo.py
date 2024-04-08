"""Run 'streamlit run app.py' in the terminal to start the app.
"""
import streamlit as st
import leafmap.foliumap as leafmap
# st.set_page_config(layout="wide")

"# leafmap streamlit demo"
st.markdown('Source code: <https://github.com/giswqs/leafmap-streamlit/blob/master/app.py>')



"## Load a GeoJSON file"
with st.echo():

    m = leafmap.Map(center=[0, 0], zoom=2)
    in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable-geo.geojson'
    m.add_geojson(in_geojson, layer_name="Cable lines")
    m.to_streamlit()





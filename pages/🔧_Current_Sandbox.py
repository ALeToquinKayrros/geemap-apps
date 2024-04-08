import streamlit as st
import leafmap.foliumap as leafmap
import leafmap.colormaps as cm


# st.set_page_config(layout="wide")

"## Bienvenue sur cette page!"

with st.echo():
    m = leafmap.Map(center=[40, -100], zoom=4)
    m.add_tile_layer(
        url="https://wxs.ign.fr/topographie/geoportail/tms/1.0.0/BDTOPO/%7Bz%7D/%7Bx%7D/%7By%7D.pbf",
        name="BDTOPO",
        attribution="IGN",
    )
    m.to_streamlit()

    "## Flux WMS"
with st.echo():
    m = leafmap.Map(center=[40, -100], zoom=4, height='500px')
    url = 'https://data.geopf.fr/annexes/ressources/wms-r/clc.xml'
    m.add_wms_layer(
        url=url,
        layers='LANDCOVER.CHA18_FR',

    )
    m.to_streamlit()

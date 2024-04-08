import streamlit as st
import leafmap.foliumap as leafmap
from PIL import Image
import tempfile
import os

# Set the page layout
# st.set_page_config(layout="wide")

# Title
st.markdown("## Bienvenue sur cette page!")

# Raster - GeoTIFF
with st.echo(code_location="below"):
    m = leafmap.Map(center=[0, 0], zoom=2)
    
    # File uploader for raster image
    uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg", "tif", "tiff"])
    
    if uploaded_file is not None:
        # Read the uploaded image file
        image = Image.open(uploaded_file)
        
        # Display the image using Streamlit
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Create a temporary directory to store the uploaded file
        temp_dir = tempfile.mkdtemp()
        
        # Save the uploaded file to the temporary directory
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Add the raster layer to the map
        m.add_raster(file_path, band=[1,2,3], vmin=1, vmax=200, layer_name="Raster")
        
        # Display the map in Streamlit
        m.to_streamlit()



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

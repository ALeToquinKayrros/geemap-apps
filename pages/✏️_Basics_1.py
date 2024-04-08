"""Run 'streamlit run app.py' in the terminal to start the app.
"""
import streamlit as st
import leafmap.foliumap as leafmap

# st.set_page_config(layout="wide")

"## Flux XYZ"
with st.echo():
    m = leafmap.Map(center=[40, -100], zoom=4)
    m.add_tile_layer(
        url="https://a.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",
        name="OpenStreetMap.HOT",
        attribution="OpenStreetMap",
    )
    m.to_streamlit()

"## Flux WMS"
with st.echo():
    m = leafmap.Map(center=[40, -100], zoom=4, height='500px')
    url = 'https://imagery.nationalmap.gov/arcgis/services/USGSNAIPPlus/ImageServer/WMSServer?'
    m.add_wms_layer(
        url=url,
        layers='USGSNAIPPlus:NaturalColor',
        name='NAIP',
        format='image/png',
        attribution='USGS',
        transparent=True,
    )
    m.to_streamlit()

"##  Vector - Points"
with st.echo():
    cities = 'https://open.gishub.org/data/us/cities.geojson'
    m = leafmap.Map(center=[40, -100], zoom=4)
    m.add_geojson(cities, layer_name='Cities')
    m.to_streamlit()

"##  Vector - Lines"
with st.echo():
    cables = 'https://open.gishub.org/data/vector/cables.geojson'
    m = leafmap.Map(center=[0, 0], zoom=2)
    m.add_geojson(cables, layer_name="Submarine Cables", zoom_to_layer=False)
    m.to_streamlit()

"##  Vector - Polygons"
with st.echo():
    countries = "https://open.gishub.org/data/world/countries.geojson"
    style = {
    "stroke": True,
    "color": "#0000ff",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "#0000ff",
    "fillOpacity": 0.1,
    }
    hover_style = {"fill": True, "fillColor": "#fc0303", "fillOpacity": 0.5}  # Doesnt work for some reason
    m = leafmap.Map(center=[0, 0], zoom=2)
    m.add_geojson(countries, layer_name="Countries", style=style, hover_style=hover_style)
    m.to_streamlit()

"##  Raster - GeoTIFF"
with st.echo():
    m = leafmap.Map(center=[0, 0], zoom=2)
    landsat = 'landsat.tif'
    landsat_url = 'https://open.gishub.org/data/raster/landsat.tif'
    leafmap.download_file(url=landsat_url, output=landsat)

    m.add_raster(landsat, band=[4, 3, 2], vmin=1, vmax=100, layer_name="Landsat")
    m.to_streamlit()

"## COGS"
with st.echo():
    import os
    os.environ['TITILER_ENDPOINT'] = 'https://titiler.xyz'

    url = 'https://opendata.digitalglobe.com/events/california-fire-2020/pre-event/2018-02-16/pine-gulch-fire20/1030010076004E00.tif'

    m = leafmap.Map()
    m.add_cog_layer(url, name="Fire (pre-event)")

    url2 = 'https://opendata.digitalglobe.com/events/california-fire-2020/post-event/2020-08-14/pine-gulch-fire20/10300100AAC8DD00.tif'
    m.add_cog_layer(url2, name="Fire (post-event)")
    m.to_streamlit()
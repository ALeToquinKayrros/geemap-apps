"""Run 'streamlit run app.py' in the terminal to start the app.
"""
import streamlit as st
import leafmap.foliumap as leafmap
import leafmap.colormaps as cm


# st.set_page_config(layout="wide")

"## Legende"
with st.echo(code_location="below"):
    m = leafmap.Map(center=[40, -100], zoom=4)
    m.add_basemap('Esri.WorldImagery')
    m.add_basemap('NLCD 2021 CONUS Land Cover')

    #Recuperation en ligne
    #m.add_legend(builtin_legend='NLCD', title='NLCD Land Cover Type')

    #Manuel
    legend_dict = {
    '00 Test': '000000',
    '11 Open Water': '466b9f',
    '12 Perennial Ice/Snow': 'd1def8',
    '21 Developed, Open Space': 'dec5c5',
    '22 Developed, Low Intensity': 'd99282',
    '23 Developed, Medium Intensity': 'eb0000',
    '24 Developed High Intensity': 'ab0000',
    '31 Barren Land (Rock/Sand/Clay)': 'b3ac9f',
    '41 Deciduous Forest': '68ab5f',
    '42 Evergreen Forest': '1c5f2c',
    '43 Mixed Forest': 'b5c58f',
    '51 Dwarf Scrub': 'af963c',
    '52 Shrub/Scrub': 'ccb879',
    '71 Grassland/Herbaceous': 'dfdfc2',
    '72 Sedge/Herbaceous': 'd1d182',
    '73 Lichens': 'a3cc51',
    '74 Moss': '82ba9e',
    '81 Pasture/Hay': 'dcd939',
    '82 Cultivated Crops': 'ab6c28',
    '90 Woody Wetlands': 'b8d9eb',
    '95 Emergent Herbaceous Wetlands': '6c9fb8',
    }
    m.add_legend(title="NLCD Land Cover Type", legend_dict=legend_dict)
    m.to_streamlit()


"##  Colorbar + labels"
with st.echo(code_location="below"):
    m = leafmap.Map(center=[40, -100], zoom=4)

    ###Colorbar
    m.add_basemap('USGS 3DEP Elevation')
    #Est il possible d'importer la colorbar directement? A essayer...
    colors = ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
    vmin = 0
    vmax = 4000
    m.add_colorbar(colors=colors, vmin=vmin, vmax=vmax,caption="Colorbar cree manuellement")

    ###US States shape+label
    data = "https://open.gishub.org/data/us/us_states.geojson"
    style = {
    "stroke": True,
    "color": "#0000ff",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "#0000ff",
    "fillOpacity": 0.05,
    }
    
    m.add_geojson(data, layer_name="States", style=style)
    m.add_labels(
        data,
        "id",
        font_size="12pt",
        font_color="blue",
        font_family="arial",
        font_weight="bold",
    )

    m.to_streamlit()


"##  Split bar"
with st.echo():
    m = leafmap.Map(center=[36.1, -114.9], zoom=10)
    ##Ne marche pas bien
    m.split_map(
        left_layer="NLCD 2001 CONUS Land Cover",
        right_layer="NLCD 2021 CONUS Land Cover",
        left_label="2001",
        right_label="2021",
        add_close_button=False,
    )
    m.to_streamlit()


"## Create a heat map"
with st.echo():
    m = leafmap.Map(tiles='stamentoner', attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.')

    m.add_basemap('TERRAIN')
    m.add_basemap('SATELLITE')
    m.add_basemap("Esri.NatGeoWorldMap") #We can also use Leafmap included basemaps
    

    filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    
    m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="pop_max", name="Heat map", radius=20)
    m.to_streamlit(width=700, height=500, add_layer_control=True)


"## Create a 3D map using Kepler.gl"
with st.echo():
    import streamlit as st
    import leafmap.kepler as leafmap

    m = leafmap.Map(center=[37.7621, -122.4143], zoom=12)
    in_csv = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/hex_data.csv'
    config = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/hex_config.json'
    m.add_csv(in_csv, layer_name="hex_data", config=config)
    m.to_streamlit()

    
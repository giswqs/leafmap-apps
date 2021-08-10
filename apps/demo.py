"""Run 'streamlit run app.py' in the terminal to start the app.
"""
import streamlit as st

# st.set_page_config(layout="wide")

def app():

    "# leafmap streamlit demo"
    st.markdown('Source code: <https://github.com/giswqs/leafmap-streamlit/blob/master/app.py>')

    "## Create a 3D map using Kepler.gl"
    with st.echo():
        import leafmap.kepler as leafmap

        m = leafmap.Map(center=[37.7621, -122.4143], zoom=12)
        in_csv = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/hex_data.csv'
        config = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/hex_config.json'
        m.add_csv(in_csv, layer_name="hex_data", config=config)
        m.to_streamlit()


    "## Create a heat map"
    with st.echo():
        import leafmap.foliumap as leafmap

        filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
        m = leafmap.Map(tiles='stamentoner')
        m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="pop_max", name="Heat map", radius=20)
        m.to_streamlit(width=700, height=500, add_layer_control=True)
        

    "## Load a GeoJSON file"
    with st.echo():

        m = leafmap.Map(center=[0, 0], zoom=2)
        in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable-geo.geojson'
        m.add_geojson(in_geojson, layer_name="Cable lines")
        m.to_streamlit()


    "## Add a colorbar"
    with st.echo():

        m = leafmap.Map()
        m.add_basemap('USGS 3DEP Elevation')
        colors = ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
        vmin = 0
        vmax = 4000
        m.add_colorbar(colors=colors, vmin=vmin, vmax=vmax)
        m.to_streamlit()


    "## Change basemaps"
    with st.echo():
        m = leafmap.Map()
        m.add_basemap("Esri.NatGeoWorldMap")
        m.to_streamlit()



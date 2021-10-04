import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Change basemaps")

    keys = list(leafmap.folium_basemaps.keys())[1:]

    basemap = st.selectbox("Select a basemap", keys)

    code = f"""import leafmap
m = leafmap.Map()
m.add_basemap('{basemap}')
m"""
    st.code(code)

    m = leafmap.Map()
    m.add_basemap(basemap)
    m.to_streamlit()

import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Basemaps")

    keys = list(leafmap.folium_basemaps.keys())[1:]

    basemap = st.selectbox("Select a basemap", keys)

    m = leafmap.Map()
    m.add_basemap(basemap)
    m.to_streamlit()

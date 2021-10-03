import streamlit as st
import leafmap


def app():
    st.title("Add vector datasets")

    url = "https://raw.githubusercontent.com/giswqs/data/main/world/world_cities.csv"
    in_csv = st.text_input("Enter a URL to a vector file", url)

    m = leafmap.Map()

    if in_csv:
        m.add_xy_data(in_csv, x="longitude", y="latitude", layer_name="World Cities")

    m.to_streamlit()

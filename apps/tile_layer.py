import streamlit as st


def app():

    st.title("Add tile layers")

    st.header("Add XYZ tile layer")

    with st.echo():
        import leafmap.foliumap as leafmap

        m = leafmap.Map()
        m.add_tile_layer(
            url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
            name="Google Satellite",
            attribution="Google",
        )
        m.to_streamlit()

    st.header("Add WMS tile layer")
    with st.echo():
        import leafmap.foliumap as leafmap

        m = leafmap.Map()
        naip_url = "https://services.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?"
        m.add_wms_layer(
            url=naip_url,
            layers="0",
            name="NAIP Imagery",
            format="image/png",
            shown=True,
        )
        m.to_streamlit()

    st.header("Add xyzservices provider")
    with st.echo():
        import os
        import leafmap.foliumap as leafmap
        import xyzservices.providers as xyz

        basemap = xyz.HEREv3.basicMap
        basemap["apiKey"] = os.environ["HEREMAPS_API_KEY"]
        m = leafmap.Map()
        m.add_basemap(basemap)
        m.to_streamlit()

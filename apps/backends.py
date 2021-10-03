import streamlit as st


def app():

    st.title("Plotting backends")

    backend = st.selectbox(
        "Select a plotting backend", ["ipyleaflet", "folium", "heremap", "keperl.gl"]
    )

    if backend == "ipyleaflet":
        import leafmap.leafmap as leafmap
    elif backend == "folium":
        import leafmap.foliumap as leafmap
    elif backend == "heremap":
        import leafmap.heremap as leafmap
    elif backend == "keperl.gl":
        import leafmap.kepler as leafmap

    m = leafmap.Map()
    m.to_streamlit()

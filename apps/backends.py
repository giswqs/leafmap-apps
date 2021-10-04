import streamlit as st


def app():

    st.title("Plotting backends")

    backend = st.selectbox(
        "Select a plotting backend",
        ["ipyleaflet", "folium", "heremap", "keperl.gl"],
        index=1,
    )

    if backend == "ipyleaflet":
        with st.echo():
            import leafmap.leafmap as leafmap
    elif backend == "folium":
        with st.echo():
            import leafmap.foliumap as leafmap
    elif backend == "heremap":
        with st.echo():
            import leafmap.heremap as leafmap
    elif backend == "keperl.gl":
        with st.echo():
            import leafmap.kepler as leafmap

    with st.echo():
        m = leafmap.Map()
        m.to_streamlit()

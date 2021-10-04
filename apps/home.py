import streamlit as st


def app():
    st.title("Home")

    st.header("Introduction")
    st.write(
        "This web app demonstrates how to create interactive maps using leafmap and streamlit."
    )

    st.markdown("Source code: <https://github.com/giswqs/leafmap-apps>")
    st.markdown("Web app: <https://gishub.org/leafmap-apps>")

    st.header("Example")

    with st.echo():
        import leafmap.foliumap as leafmap

        filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
        m = leafmap.Map(tiles="stamentoner")
        m.add_heatmap(
            filepath,
            latitude="latitude",
            longitude="longitude",
            value="pop_max",
            name="Heat map",
            radius=20,
        )
        m.to_streamlit(width=700, height=500)

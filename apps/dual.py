import streamlit as st
# import leafmap
import leafmap.foliumap as leafmap

def app():
    st.title('Folium Demo')

    page = st.radio("Select map type", ["Single map", "Dual map"], index=0)

    # center on Liberty Bell
    if page == "Single map":
        m = leafmap.Map(location=[39.949610, -75.150282], zoom_start=16)
    elif page == "Dual map":
        m = leafmap.Map()
    # components.html(m.to_html(), height=800)
    m.to_streamlit(height=600)

    # m.to_streamlit()
    # # add marker for Liberty Bell
    # tooltip = "Liberty Bell"
    # folium.Marker(
    #     [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    # ).add_to(m)

    # # call to render Folium map in Streamlit
    # folium_static(m)
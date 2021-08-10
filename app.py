import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats, demo, dual, uber_nyc # import your app modules here

st.set_page_config(layout="wide")


app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Demo", demo.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Dual", dual.app)
app.add_app("Pydeck", uber_nyc.app)

# The main app
app.run()
import streamlit as st
from multiapp import MultiApp
from apps import (
    home,
    backends,
    data_stats,
    demo,
    dual,
    uber_nyc,
)

# st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here
apps.add_app("Home", home.app)
apps.add_app("Plotting backends", backends.app)
apps.add_app("Demo", demo.app)
apps.add_app("Data Stats", data_stats.app)
apps.add_app("Dual", dual.app)
apps.add_app("Pydeck", uber_nyc.app)

# The main app
apps.run()

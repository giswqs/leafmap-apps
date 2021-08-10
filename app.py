import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats, demo, dual # import your app modules here


app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Demo", demo.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Dual", dual.app)

# The main app
app.run()
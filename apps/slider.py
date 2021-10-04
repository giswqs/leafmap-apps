import streamlit as st
import random


def app():

    def _update_slider(value):
        st.session_state["test_slider"] = value

    if "test_slider" not in st.session_state:
        st.session_state["test_slider"] = 0

    slider = st.slider("My slider", key="test_slider",
                       min_value=-100, max_value=100)

    st.write("Current value:", slider)

    st.button("Update slider values", on_click=_update_slider,
              kwargs={"value": random.randint(-100, 100)})

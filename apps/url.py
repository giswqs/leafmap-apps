import streamlit as st

st.title("Experimental: Play with Query Strings!")

app_state = st.experimental_get_query_params()
app_state = {k: v[0] if isinstance(v, list) else v for k, v in app_state.items()} # fetch the first item in each query string as we don't have multiple values for each query string key in this example

# [1] Checkbox
default_checkbox = eval(app_state["checkbox"]) if "checkbox" in app_state else False
checkbox1 = st.checkbox("Are you really happy today?", key="checkbox1", value = default_checkbox)
app_state["checkbox"] = checkbox1
st.experimental_set_query_params(**app_state)
st.markdown("")


# [2] Radio
radio_list = ['Eat', 'Sleep', 'Both']
default_radio = int(app_state["radio"]) if "radio" in app_state else 0
genre = st.radio("What are you doing at home during quarantine?", radio_list, index = default_radio)
if genre:
    app_state["radio"] = radio_list.index(genre)
    st.experimental_set_query_params(**app_state)
st.markdown("")


# [3] Text Input
default_title = app_state["movie"] if "movie" in app_state else ""
title = st.text_input('Movie title', value = default_title)
app_state["movie"] = title
st.experimental_set_query_params(**app_state)


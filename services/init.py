import streamlit as st


def init_state():
    if "title" not in st.session_state:
        st.session_state.title = "Lamda Store"

    if "choice" not in st.session_state:
        st.session_state.choice = "Sign in"

import streamlit as st

def init_state():
    if "title" not in st.session_state:
        st.session_state.title = "Lamda Store"

    if "choice" not in st.session_state:
        st.session_state.choice = "Sign in"

    if "menu" not in st.session_state:
        st.session_state.menu = ["Sign in", "Sign up"]

    if "product_choice" not in st.session_state:
        st.session_state.product_choice = None
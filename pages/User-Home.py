import streamlit as st

from wirpl_books.services.user import UserService

st.set_page_config(page_title="User Home", page_icon="📈")

st.markdown("# User Home")

user_service = UserService(st.session_state)

if not user_service.is_logged_in:
    st.switch_page("./pages/User-Login.py")

st.markdown(f"Hello {user_service.customer['name']}, welcome to your home page!")

st.page_link("./pages/User-Catalog.py", label="Catalog", icon="📚")

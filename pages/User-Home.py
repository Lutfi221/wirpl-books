import streamlit as st
import time
import numpy as np
import pandas as pd

from wirpl_books.services.user import UserService

st.set_page_config(page_title="User Home", page_icon="📈")

st.markdown("# User Home")

user_service = UserService(st.session_state)

if user_service.is_logged_in:
    st.markdown(f"Hello {user_service.customer['name']}, welcome to your home page!")
else:
    st.switch_page("./pages/User-Login.py")

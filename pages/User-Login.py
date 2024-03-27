import streamlit as st
import time
import numpy as np
import pandas as pd

from wirpl_books.models.customer import CustomerModel
from wirpl_books.services.user import UserService

st.set_page_config(page_title="Login", page_icon="📈")

st.markdown("# Login")
st.sidebar.header("Login")

user_service = UserService(st.session_state)
customer_model = CustomerModel()

with st.container():
    with st.form(key="login"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Submit")

        if submit:
            customer = user_service.login(email)
            if customer:
                st.success(f"Welcome, {user_service.customer['name']}!")
                st.switch_page("./pages/User-Home.py")
            else:
                st.error("Invalid email or password")
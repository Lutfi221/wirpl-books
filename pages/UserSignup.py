import streamlit as st

from services.user import UserService


user_service = UserService(st.session_state)
# Pakai `int(time.time())` untuk membuat ID unik
# user_service.register(int(time.time()), "John Doe", "123 Main St", "john.doe@example", "M")

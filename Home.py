import os
import sys
import streamlit as st
from pathlib import Path


CURR_DIR_PATH = Path(__file__).resolve().parents[0]

sys.path.append(str(CURR_DIR_PATH.parents[0]))

st.set_page_config(
    page_title="LAMDA Store",
    page_icon="👋",
)

st.write("# LAMBDA Book Store")

st.sidebar.success("Select a page to view")

st.markdown(
    """
 - **L**utfi Azis Hafiizhudin	(23/532366/NPA/19946)
 - **A**ndreas Notokusumo	(22/493183/PA/21167)
 - **M**ilzam Hakim Ayyasi	(22/496405/PA/21339)
 - **D**hanada Santika Putri	(22/497239/PA/21407)
 - **A**isyah Putri Khurin'in	(22/493908/PA/21227)
"""
)

import streamlit as st
import time
import numpy as np
import pandas as pd

from models.product import ProductModel
from services.user import UserService

st.set_page_config(page_title="User Catalog", page_icon="📇")

st.markdown("# Shopping Catalog")

user_service = UserService(st.session_state)

# Shopping Cart
st.sidebar.markdown("# Shopping Cart")
st.sidebar.button("Clear Cart", on_click=lambda: user_service.products.clear())
if not user_service.products:
    st.sidebar.markdown("Your cart is empty.")
else:
    for product in user_service.products:
        st.sidebar.write(product["title"])
    st.sidebar.markdown(
        f"Total: Rp{sum([p['price'] for p in user_service.products]):,}"
    )
    if st.sidebar.button("Checkout"):
        st.sidebar.write("Checkout not implemented")


product_model = ProductModel()

df_products = pd.DataFrame(product_model.get_all())
COLUMNS = ["Title", "Price", "Cart", "Details"]

for col, field in zip(st.columns(len(COLUMNS)), COLUMNS):
    col.write(field)

btn_id_count = 0
for _, row in df_products.iterrows():
    st_cols = st.columns(len(COLUMNS))
    st_cols[0].write(row["title"])
    st_cols[1].write(row["price"])
    st_cols[2].button(
        "Add to Cart",
        key=f"btn_add2cart_{btn_id_count}",
        on_click=lambda row: user_service.products.append(row),
        args=[row],
    )
    if st_cols[3].toggle(
        "Details",
        key=f"btn_details_{btn_id_count}",
        args=[row],
    ):
        st.write(f"Title: {row['title']}")
        st.write(row)

    btn_id_count += 1

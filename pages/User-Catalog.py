import streamlit as st
import time
import numpy as np
import pandas as pd

from wirpl_books.models.product import ProductModel


st.set_page_config(page_title="User Catalog", page_icon="📇")

st.markdown("# Shopping Catalog")

product_model = ProductModel()

df_products = pd.DataFrame(product_model.get_all())

COLUMNS = ["Title", "Price", "Cart", "Details"]

st_cols = st.columns(len(COLUMNS))

for col, field in zip(st_cols, COLUMNS):
    col.write(field)

btn_id_count = 0
for _, row in df_products.iterrows():

    st_cols[0].write(row["title"])
    st_cols[1].write(row["price"])
    st_cols[2].button("Add to Cart", key=f"btn_add2cart_{btn_id_count}")
    st_cols[3].button("Details", key=f"btn_details_{btn_id_count}")

    btn_id_count += 1

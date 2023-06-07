import pandas as pd
import streamlit as st

st.write("TEST")
master_path = "https://github.com/jayaraj-kirienergy/TRS-INVENTORY/blob/main/database/MASTER_DATA.xlsx"
master_df = pd.read_excel(master_path)

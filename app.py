import pandas as pd
import streamlit as st

st.write("TEST")
master_path = "https://github.com/jayaraj-kirienergy/TRS-INVENTORY/blob/main/database/MASTER_DATA.xlsx?raw=True"
unique_path = "https://github.com/jayaraj-kirienergy/TRS-INVENTORY/blob/main/database/UNIQUE_ID.xlsx?raw=True"
project_path = "https://github.com/jayaraj-kirienergy/TRS-INVENTORY/blob/main/database/PROJECTS.xlsx?raw=True"

unique_df = pd.read_excel(unique_path)
project_df = pd.read_excel(project_path)
master_df = pd.read_excel(master_path)

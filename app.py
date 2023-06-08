import pandas as pd
import streamlit as st
import datetime
from datetime import date
import openpyxl

st.title("KIRI AND COMPANY LOGISTICS PVT LTD - TRS INVENTORY MANAGEMENT")
master_path = "https://github.com/jayaraj-kirienergy/TRS-INVENTORY/blob/main/database/MASTER_DATA.xlsx?raw=True"
unique_path = "https://github.com/jayaraj-kirienergy/TRS-INVENTORY/blob/main/database/UNIQUE_ID.xlsx?raw=True"
project_path = "https://github.com/jayaraj-kirienergy/TRS-INVENTORY/blob/main/database/PROJECTS.xlsx?raw=True"
today = date.today()

unique_df = pd.read_excel(unique_path)
project_df = pd.read_excel(project_path)
master_df = pd.read_excel(master_path)


inp_assert_id = st.text_input("ENTER THE ASSERT-NO ",)
button1 = st.button("UPDATE-INVENTORY")
button2 = st.button("SERVICE-TICKET GENERATION")

if button1:
      st.write(inp_assert_id)
      st.write("reached till here")
      st.write(inp_assert_id)
      temp_master_df = master_df.drop_duplicates(subset=['ASSERT_NO'],keep = 'last')
      st.write("reached till here")
      s = pd.Series(list(temp_master_df['ASSERT_NO']))
      st.write(s)
      if inp_assert_id in s.values:
        ind = temp_master_df[temp_master_df['ASSERT_NO']==inp_assert_id].index.values
        need_line = temp_master_df.loc[ind]
        need_line['OUTWARD_DATE'] = pd.to_datetime(need_line['OUTWARD_DATE'],errors='coerce')
        need_line['INWARD_DATE'] = pd.to_datetime(need_line['INWARD_DATE'],errors='coerce')
        #print(need_line[['ASSERT_NO','DESCRIPTION','OUTWARD_DATE','INWARD_DATE']])
        if need_line.loc[ind,'INWARD_DATE'].notnull().any() & need_line.loc[ind,'OUTWARD_DATE'].isnull().any():
          a = "AT KIRI YARD"
          st.write(a)
          out_date = st.date_input('OUTWARD-DATE:',today)
          out_challan = st.text_input('OUTWARD - CHALLAN :')
          need_line.loc[ind,'CHALLAN_2'] = out_challan
          need_line.loc[ind,'OUTWARD_DATE'] = out_date
          st.dataframe(need_line)

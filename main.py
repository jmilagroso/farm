import pandas as pd
import streamlit as st

sheet_id   = st.secrets["google-spreadsheet"]["sheet_id"]
sheet_name = st.secrets["google-spreadsheet"]["sheet_name"]

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)

lot_area_sqm = df['lot_area_sqm'].drop_duplicates()
lot_area_sqm_choice = st.sidebar.selectbox('Lot Area (sqm):', lot_area_sqm)

tcp = df['tcp'].drop_duplicates()
tcp_choice = st.sidebar.selectbox('TCP:', tcp)

st.dataframe(df)

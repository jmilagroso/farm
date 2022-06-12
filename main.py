import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

st.set_page_config(layout="wide")

sheet_id   = st.secrets["google-spreadsheet"]["sheet_id"]
sheet_name = st.secrets["google-spreadsheet"]["sheet_name"]

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)

lot_area_sqm = df['lot_area_sqm'].drop_duplicates()
lot_area_sqm = pd.concat([pd.Series(['Filter by lot area']), lot_area_sqm])
lot_area_sqm_choice = st.sidebar.selectbox('', lot_area_sqm)

st.sidebar.text('Reservation Fee: Php 30,000.00\nComputation: 70% Loan, 30% DP\nInclusions: 1 BR Nipa Hut,\n5 Goats,\n10 Native Chickens,\n1 Pair Turkey,\n2 Buddah Bamboo Poles')

st.sidebar.text('Contact Info: +639560861684\n+639917285314\n+639760445567')

if lot_area_sqm_choice != 'Filter by lot area':
  df = df.query(f'lot_area_sqm == {lot_area_sqm_choice}')

st.dataframe(df)

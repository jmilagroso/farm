import pandas as pd
import streamlit as st
from IPython.display import display, HTML

sheet_id   = st.secrets["google-spreadsheet"]["sheet_id"]
sheet_name = st.secrets["google-spreadsheet"]["sheet_name"]

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)

st.text('Reservation Fee : Php 30,000.00')
st.text('Inclusions: 1BR Nipa Hut, 5 goats, 10 native chickens, 1 pair Turkey, 2 Buddah Bamboo Poles')
st.text('Computation: 70% Loan, 30% DP')
st.text('Contact: +639560861684, +639917285314, +63976 044 5567')

lot_area_sqm = df['lot_area_sqm'].drop_duplicates()
lot_area_sqm = pd.concat([pd.Series(['All']), lot_area_sqm])
lot_area_sqm_choice = st.selectbox('Lot Area (sqm):', lot_area_sqm)

if lot_area_sqm_choice != 'All':
  df = df.query(f'lot_area_sqm == {lot_area_sqm_choice}')

st.dataframe(df)

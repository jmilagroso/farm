import pandas as pd
import streamlit as st
from IPython.display import display, HTML

st.set_page_config(layout="wide")

sheet_id   = st.secrets["google-spreadsheet"]["sheet_id"]
sheet_name = st.secrets["google-spreadsheet"]["sheet_name"]

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)

lot_area_sqm = df['lot_area_sqm'].drop_duplicates()
lot_area_sqm = pd.concat([pd.Series(['All']), lot_area_sqm])
lot_area_sqm_choice = st.selectbox('Lot Area (sqm):', lot_area_sqm)

if lot_area_sqm_choice != 'All':
  df = df.query(f'lot_area_sqm == {lot_area_sqm_choice}')

st.dataframe(df)

st.text('''
Inclusions:
1BR Nipa Hut
5 goats
10 native chickens
1pair Turkey
2 Buddah Bamboo Poles
'''
st.text('Computation: 70% Loan, 30% DP')
st.text('Contact: +63 956 086 1684\n+63991 728 5314\n+63976 044 5567')

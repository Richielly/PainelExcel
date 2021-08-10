import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")
if uploaded_file:
    dados = pd.read_excel(uploaded_file)
    dados = pd.read_excel(uploaded_file, header=None, skiprows=1)
    dados.dropna(axis=1, how='all')
    dados.dropna(axis=0, how='all')
    dados.notna()
    st.dataframe(dados)
    st.table(dados)


#     #df.loc[:, ~df.columns.str.contains('^Unnamed')]
#     st.dataframe(df)
#     st.table(df)

import streamlit as st
import pandas as pd

st.title("📤 Upload CSV File")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state.df = df  # ✅ Store the DataFrame in session_state
    st.success("✅ File uploaded and saved in session.")
    st.dataframe(df.head())
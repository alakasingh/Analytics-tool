import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import configure_page


configure_page()

st.title("📊 Data Insights")

# ✅ Check if data exists in session_state
if "df" in st.session_state:
    df = st.session_state.df
    st.subheader("👀 First 5 Rows of the Uploaded Data")
    st.dataframe(df.head())

    st.markdown("---")
    st.header("🧠 Advanced Insights")

    # 1️⃣ Correlation Heatmap
    st.subheader("1️⃣ Correlation Heatmap (Numerical Features)")
    numeric_df = df.select_dtypes(include='number')

    if not numeric_df.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("📉 No numerical columns found for correlation heatmap.")

    # 2️⃣ Top Features Impacting Total (based on correlation)
    if "Total" in numeric_df.columns:
        st.subheader("2️⃣ Features Most Correlated with Total")
        corr_total = numeric_df.corr()["Total"].sort_values(ascending=False).drop("Total")
        st.bar_chart(corr_total)
    else:
        st.warning("⚠️ Column `Total` not found for advanced correlation.")

    # 3️⃣ Time-based Trend (if 'Date' or 'Time' exists)
    if "Date" in df.columns:
        st.subheader("3️⃣ Daily Sales Trend")
        df["Date"] = pd.to_datetime(df["Date"])
        daily_sales = df.groupby("Date")["Total"].sum().reset_index()
        fig2 = px.line(daily_sales, x="Date", y="Total", title="Total Sales Over Time", markers=True)
        st.plotly_chart(fig2)
    else:
        st.info("ℹ️ Add a `Date` column to analyze trends over time.")

else:
    st.warning("⚠️ No data found. Please upload a file in the Upload tab first.")

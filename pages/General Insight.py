import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


import plotly.express as px

st.title("📊 General Insights")

# ✅ Check if data exists in session_state
if "df" in st.session_state:
    df = st.session_state.df
    st.subheader("👀 First 5 Rows of the Uploaded Data")
    st.dataframe(df.head())

    st.markdown("---")
    st.header("📦 Product Insights")

    # Check if 'Date' column exists
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.month_name()
        df['DayOfWeek'] = df['Date'].dt.day_name()
    else:
        st.error("The 'Date' column is missing from the dataset.")

    # Check if 'Time' column exists
    if 'Time' in df.columns:
        df['Hour'] = pd.to_datetime(df['Time']).dt.hour
    else:
        st.error("The 'Time' column is missing from the dataset.")

    # Check if 'City' column exists
    if 'City' in df.columns:
        st.sidebar.header("Filters")
        selected_city = st.sidebar.multiselect("Select City", df["City"].unique(), default=df["City"].unique())
        filtered_df = df[df["City"].isin(selected_city)]

       

        if 'DayOfWeek' in df.columns and 'Total' in df.columns:
            st.subheader("🛍️ Sales by Day of the Week")
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.barplot(x=filtered_df["DayOfWeek"], y=filtered_df["Total"], estimator=sum, ax=ax, palette="viridis")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        if 'Product line' in df.columns:
            st.subheader("📦 Sales by Product Line")
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.countplot(y=filtered_df["Product line"], order=filtered_df["Product line"].value_counts().index, palette="coolwarm")
            st.pyplot(fig)

        if 'Date' in df.columns and 'Total' in df.columns:
            st.subheader("📅 Sales Trend Over Time")
            fig, ax = plt.subplots(figsize=(10, 5))
            filtered_df.groupby("Date")["Total"].sum().plot(ax=ax)
            ax.set_ylabel("Total Sales")
            st.pyplot(fig)

        if 'Hour' in df.columns and 'Total' in df.columns:
            st.subheader("⏰ Peak Shopping Hours")
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.barplot(x=filtered_df["Hour"], y=filtered_df["Total"], estimator=sum, ax=ax, palette="pastel")
            st.pyplot(fig)
    else:
        st.error("The 'City' column is missing from the dataset.")
else:
    st.warning("No dataset found. Please upload your data on the main page.")

    # Footer in Sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("🔗 **Follow me on GitHub:** [GitHub ID](https://github.com/alakasingh)")

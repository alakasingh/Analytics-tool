import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Data Insights")

# ✅ Check if data exists in session_state
if "df" in st.session_state:
    df = st.session_state.df
    st.subheader("👀 First 5 Rows of the Uploaded Data")
    st.dataframe(df.head())

    st.markdown("---")
    st.header("⏱️ Time-based Customer Insights")

    # Required columns
    time_cols = ["Time", "Date", "Total"]
    if all(col in df.columns for col in time_cols):

        # Convert Time and Date columns
        df["Time"] = pd.to_datetime(df["Time"], format="mixed", errors="coerce").dt.time
        df["Hour"] = pd.to_datetime(df["Time"].astype(str), format="%H:%M:%S").dt.hour
        df["Date"] = pd.to_datetime(df["Date"])
        df["Day"] = df["Date"].dt.day_name()

        # 1. 🔥 Peak Hour
        st.subheader("🔥 Peak Hour for Sales")
        sales_per_hour = df.groupby("Hour")["Total"].sum().reset_index()
        
        # Check if sales_per_hour is not empty before plotting
        if not sales_per_hour.empty:
            fig1 = px.bar(sales_per_hour, x="Hour", y="Total", title="Total Sales by Hour",
                          color="Total", color_continuous_scale="Viridis")
            st.plotly_chart(fig1)

            peak_hour = sales_per_hour.sort_values(by="Total", ascending=False).iloc[0]
            st.success(f"⏰ **Peak Hour:** {peak_hour['Hour']}:00 with total sales of ${peak_hour['Total']:.2f}")
        else:
            st.warning("⚠️ No sales data available for peak hour analysis.")

        # 2. ⏰ Sales by Time Slot
        st.subheader("🕒 Sales by Time Slot")

        def assign_time_slot(hour):
            if 5 <= hour < 12:
                return "Morning"
            elif 12 <= hour < 17:
                return "Afternoon"
            elif 17 <= hour < 21:
                return "Evening"
            else:
                return "Night"

        df["Time Slot"] = df["Hour"].apply(assign_time_slot)
        slot_sales = df.groupby("Time Slot")["Total"].sum().reset_index()
        fig2 = px.pie(slot_sales, names="Time Slot", values="Total", title="Sales by Time Slot",
                      color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig2)

        # 3. 📊 Daily-Hour Heatmap
        st.subheader("📅 Heatmap: Daily Hourly Sales")

        pivot = df.pivot_table(values="Total", index="Day", columns="Hour", aggfunc="sum", fill_value=0)
        # Reorder days
        days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        pivot = pivot.reindex(days_order)

        # Check if the pivot table is empty or contains NaN values
        if pivot.isnull().values.any():
            st.warning("⚠️ Some missing data in the pivot table.")

        if pivot.size > 0:  # Ensure there's data in the pivot table
            fig3, ax = plt.subplots(figsize=(12, 5))
            sns.heatmap(pivot, cmap="YlGnBu", linewidths=0.3, annot=True, fmt=".0f", ax=ax)
            st.pyplot(fig3)
        else:
            st.warning("⚠️ No data available to display in the heatmap.")

    else:
        st.error("🚫 Required columns for time-based insights not found.")
        st.markdown("Required: `Time`, `Date`, `Total`")

else:
    st.warning("⚠️ No data found. Please upload a file in the Upload tab first.")

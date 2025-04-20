import streamlit as st
import pandas as pd

st.title("📊 Data Insights")

# ✅ Check if data exists in session_state
if "df" in st.session_state:
    df = st.session_state.df

    st.subheader("👀 First 5 Rows of the Uploaded Data")
    st.dataframe(df.head())

    st.markdown("---")
    st.header("🏢 Branch-Level Insights")

    required_columns = ["Branch", "Total"]

    # ✅ Check if required columns exist
    if all(col in df.columns for col in required_columns):
        # 1. Revenue per branch
        st.subheader("💰 Revenue per Branch")
        revenue_per_branch = df.groupby("Branch")["Total"].sum().reset_index()
        st.dataframe(revenue_per_branch)

        # 2. 🏆 Top performing branch (by revenue)
        top_branch = revenue_per_branch.sort_values(by="Total", ascending=False).iloc[0]
        st.markdown("### 🏅 Top Performing Branch")
        st.success(
            f"🎯 **{top_branch['Branch']}** generated the highest revenue: **${top_branch['Total']:.2f}**"
        )

        # 3. 👥 Branch with the most customers (by row count)
        st.subheader("👥 Branch with Most Customers")
        customers_per_branch = df["Branch"].value_counts().reset_index()
        customers_per_branch.columns = ["Branch", "Customer Count"]
        st.dataframe(customers_per_branch)

        top_customers_branch = customers_per_branch.iloc[0]
        st.info(
            f"👑 **{top_customers_branch['Branch']}** has the most customers: **{top_customers_branch['Customer Count']}**"
        )

    else:
        st.error("🚫 Required columns not found in the uploaded dataset.")
        st.markdown("Required columns: `Branch`, `Total`")

else:
    st.warning("⚠️ No data found. Please upload a file in the Upload tab first.")

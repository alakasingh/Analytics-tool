import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Data Insights")

# ✅ Check if data exists in session_state
if "df" in st.session_state:
    df = st.session_state.df

    st.subheader("👀 First 5 Rows of the Uploaded Data")
    st.dataframe(df.head())

    st.markdown("---")
    st.header("🧍‍♂️ Customer-Level Insights")

    # Required columns
    customer_columns = ["Gender", "Total", "Customer type", "Rating"]

    if all(col in df.columns for col in customer_columns):
        # 1. 🎯 Gender Distribution
        st.subheader("📊 Gender Distribution")
        gender_dist = df["Gender"].value_counts().reset_index()
        gender_dist.columns = ["Gender", "Count"]
        fig1 = px.bar(gender_dist, x="Gender", y="Count", color="Gender",
                      title="Gender Distribution", color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig1)

        # 2. 💰 Sales by Gender
        st.subheader("💰 Sales by Gender")
        sales_by_gender = df.groupby("Gender")["Total"].sum().reset_index()
        fig2 = px.bar(sales_by_gender, x="Gender", y="Total", color="Gender",
                      title="Total Sales by Gender", color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig2)

        # 3. 🧾 Customer Type (Member vs Normal)
        st.subheader("👤 Customer Type Distribution")
        type_dist = df["Customer type"].value_counts().reset_index()
        type_dist.columns = ["Customer Type", "Count"]
        fig3 = px.bar(type_dist, x="Customer Type", y="Count", color="Customer Type",
                      title="Customer Type Count", color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig3)

        # 4. 💳 Average Spend per Customer Type
        st.subheader("💸 Average Spend per Customer Type")
        avg_spend = df.groupby("Customer type")["Total"].mean().reset_index()
        avg_spend.columns = ["Customer Type", "Avg Spend"]
        fig4 = px.bar(avg_spend, x="Customer Type", y="Avg Spend", color="Customer Type",
                      title="Average Spend by Customer Type", color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig4)

        # 5. ⭐ Rating Distribution and Average
        st.subheader("⭐ Rating Distribution")
        fig5 = px.histogram(df, x="Rating", nbins=10, title="Rating Distribution",
                            color_discrete_sequence=["#FFB347"])
        st.plotly_chart(fig5)

        avg_rating = df["Rating"].mean()
        st.success(f"📌 **Average Rating:** {avg_rating:.2f}")

    else:
        st.error("🚫 Required columns for customer-level insights not found.")
        st.markdown("Required columns: `Gender`, `Total`, `Customer type`, `Rating`")

else:
    st.warning("⚠️ No data found. Please upload a file in the Upload tab first.")

import streamlit as st
import plotly.express as px
from utils import configure_page


configure_page()

st.title("📊 Data Insights")

# ✅ Check if data exists in session_state
if "df" in st.session_state:
    df = st.session_state.df
    st.subheader("👀 First 5 Rows of the Uploaded Data")
    st.dataframe(df.head())

    st.markdown("---")
    st.header("📦 Product Insights")

    required_columns = ["Product line", "Total", "Quantity", "Unit price"]
    if all(col in df.columns for col in required_columns):

        # 1. 📊 Sales by Product Line
        st.subheader("1️⃣ Sales by Product Line")
        sales_by_line = df.groupby("Product line")["Total"].sum().reset_index()
        fig1 = px.bar(sales_by_line, x="Product line", y="Total", color="Product line",
                      title="Total Sales by Product Line", color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig1)

        # 2. 💲 Average Product Price per Category
        st.subheader("2️⃣ Average Product Price per Category")
        avg_price = df.groupby("Product line")["Unit price"].mean().reset_index()
        fig2 = px.bar(avg_price, x="Product line", y="Unit price", color="Product line",
                      title="Average Unit Price by Product Line", color_discrete_sequence=px.colors.qualitative.Safe)
        st.plotly_chart(fig2)

        # 3. 🔢 Total Quantity Sold by Product Line
        st.subheader("3️⃣ Total Quantity Sold per Product Line")
        quantity_by_line = df.groupby("Product line")["Quantity"].sum().reset_index()
        fig3 = px.bar(quantity_by_line, x="Product line", y="Quantity", color="Product line",
                      title="Total Quantity Sold by Product Line", color_discrete_sequence=px.colors.sequential.Agsunset)
        st.plotly_chart(fig3)

        # 4. 💹 Most Profitable Product Line
        st.subheader("4️⃣ Most Profitable Product Line")
        most_profitable = sales_by_line.sort_values(by="Total", ascending=False).iloc[0]
        st.success(f"💰 **Most Profitable Line:** {most_profitable['Product line']} with total sales of ${most_profitable['Total']:.2f}")

    else:
        st.error("🚫 Required columns for product insights not found.")
        st.markdown("Required: `Product line`, `Total`, `Quantity`, `Unit price`")

else:
    st.warning("⚠️ No data found. Please upload a file in the Upload tab first.")

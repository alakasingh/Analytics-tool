import streamlit as st
import plotly.express as px

st.title("📊 Data Insights")

# ✅ Check if data exists in session_state
if "df" in st.session_state:
    df = st.session_state.df
    st.subheader("👀 First 5 Rows of the Uploaded Data")
    st.dataframe(df.head())

    st.markdown("---")
    st.header("📎 Profit & Tax Insights")

    required_cols = ["Tax 5%", "gross income", "Product line", "Branch", "Total"]
    if all(col in df.columns for col in required_cols):

        # 1. 💰 Total Tax Collected
        st.subheader("1️⃣ Total Tax Collected")
        total_tax = df["Tax 5%"].sum()
        st.success(f"💸 **Total Tax Collected:** ${total_tax:,.2f}")

        # 2. 🏢 Gross Income by Branch
        st.subheader("2️⃣ Gross Income by Branch")
        income_branch = df.groupby("Branch")["gross income"].sum().reset_index()
        fig1 = px.bar(income_branch, x="Branch", y="gross income", color="Branch",
                      title="Gross Income by Branch", color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig1)

        # 3. 🛒 Gross Income by Product Line
        st.subheader("3️⃣ Gross Income by Product Line")
        income_product = df.groupby("Product line")["gross income"].sum().reset_index()
        fig2 = px.bar(income_product, x="Product line", y="gross income", color="Product line",
                      title="Gross Income by Product Line", color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig2)

        # 4. 📈 Profit Margin
        st.subheader("4️⃣ Profit Margin")
        
        # Per Transaction
        df["Profit Margin (%)"] = (df["gross income"] / df["Total"]) * 100
        st.markdown("📊 **Profit Margin per Transaction**")
        st.dataframe(df[["Total", "gross income", "Profit Margin (%)"]].head())

        # Average by Product Line
        avg_margin = df.groupby("Product line")["Profit Margin (%)"].mean().reset_index()
        fig3 = px.bar(avg_margin, x="Product line", y="Profit Margin (%)", color="Product line",
                      title="Average Profit Margin by Product Line", color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig3)

    else:
        st.error("🚫 Required columns for profit & tax insights not found.")
        st.markdown("Required: `Tax 5%`, `gross income`, `Product line`, `Branch`, `Total`")

else:
    st.warning("⚠️ No data found. Please upload a file in the Upload tab first.")

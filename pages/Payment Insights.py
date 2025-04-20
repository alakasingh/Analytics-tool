import streamlit as st
import plotly.express as px

st.title("📊 Data Insights")

# ✅ Check if data exists in session_state
if "df" in st.session_state:
    df = st.session_state.df
    st.subheader("👀 First 5 Rows of the Uploaded Data")
    st.dataframe(df.head())

    st.markdown("---")
    st.header("💳 Payment Insights")

    # Required columns
    if "Payment" in df.columns and "Total" in df.columns:

        # 1. 🥇 Most Popular Payment Method
        st.subheader("🥇 Most Popular Payment Method")
        payment_counts = df["Payment"].value_counts().reset_index()
        payment_counts.columns = ["Payment Method", "Count"]
        fig1 = px.bar(payment_counts, x="Payment Method", y="Count", color="Payment Method",
                      title="Most Popular Payment Methods", color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig1)

        most_popular = payment_counts.iloc[0]
        st.success(f"🏆 **Most Used:** {most_popular['Payment Method']} ({most_popular['Count']} transactions)")

        # 2. 💰 Revenue by Payment Method
        st.subheader("💰 Revenue by Payment Method")
        payment_revenue = df.groupby("Payment")["Total"].sum().reset_index()
        payment_revenue.columns = ["Payment Method", "Revenue"]
        fig2 = px.bar(payment_revenue, x="Payment Method", y="Revenue", color="Payment Method",
                      title="Revenue per Payment Method", color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig2)

        # 3. 🔁 Transaction Volume by Payment Type
        st.subheader("🔁 Transaction Volume per Payment Method")
        fig3 = px.pie(payment_counts, names="Payment Method", values="Count",
                      title="Transaction Volume Share", color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig3)

    else:
        st.error("🚫 Required columns for payment insights not found.")
        st.markdown("Required: `Payment`, `Total`")

else:
    st.warning("⚠️ No data found. Please upload a file in the Upload tab first.")

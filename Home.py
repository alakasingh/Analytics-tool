import streamlit as st
from components.header import show_header
from utils import configure_page
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Apply page configuration (must be the first Streamlit command)
configure_page()

def main():
    show_header()
    st.write("Choose a page from the sidebar to explore more features.")
    
    st.markdown("""
    **Note:** When uploading your dataset, please ensure it contains the following column names:
    - `Date`   `Time` `City` `Product line` `Total`
    """)

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df  # ✅ Store the DataFrame in session_state
        st.success("✅ File uploaded and saved in session.")

        # Show dataset preview
        if st.checkbox("Show Raw Data"):
            st.write(df)

if __name__ == "__main__":
    main()
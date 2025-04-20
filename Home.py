import streamlit as st
from components.header import show_header
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt





def main():
    st.set_page_config(
    page_title="Home",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
   )

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
   


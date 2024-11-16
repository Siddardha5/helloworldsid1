import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
print(matplotlib.__version__)

# Title
st.title("Simple Data Analysis App")

# File Uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:", data.head())

    # Show a plot
    st.write("Histogram of a Column")
    column_name = st.selectbox("Select a Column:", data.columns)
    fig, ax = plt.subplots()
    ax.hist(data[column_name], bins=20, color="blue", alpha=0.7)
    st.pyplot(fig)

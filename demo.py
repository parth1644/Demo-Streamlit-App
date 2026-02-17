import streamlit as st
import pandas as pd

st.title("CSV File Viewer")

df = pd.read_csv("data.csv")

st.write("### Dataset Preview")
st.dataframe(df)

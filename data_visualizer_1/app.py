import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="CSV Visualizer", layout="wide")

st.title("📊 CSV Data Visualizer")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")

        st.subheader("Preview of Data")
        st.dataframe(df.head())

        numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

        if numeric_columns:
            chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Histogram"])

            if chart_type == "Line Chart":
                selected_column = st.selectbox("Select Column for Line Chart", numeric_columns)
                st.line_chart(df[selected_column])

            elif chart_type == "Bar Chart":
                selected_column = st.selectbox("Select Column for Bar Chart", numeric_columns)
                st.bar_chart(df[selected_column])

            elif chart_type == "Histogram":
                selected_column = st.selectbox("Select Column for Histogram", numeric_columns)
                bins = st.slider("Number of Bins", min_value=5, max_value=50, value=10)
                fig, ax = plt.subplots()
                sns.histplot(df[selected_column], bins=bins, kde=True, ax=ax)
                st.pyplot(fig)

        else:
            st.warning("No numeric columns found to visualize.")

    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload a CSV file to start.")


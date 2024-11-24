import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import load_data, calculate_metrics, perform_ab_test

st.title("A/B Testing Web App")

st.sidebar.header("Upload your data")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=['csv'])

if uploaded_file:
    # Load and display data
    data = load_data(uploaded_file)
    st.write("### Uploaded Data")
    st.dataframe(data.head())
    
    # Display summary statistics
    st.write("### Summary Statistics")
    metrics = calculate_metrics(data)
    st.write(metrics)
    
    # Visualization
    st.write("### Conversion Rate Visualization")
    fig, ax = plt.subplots()
    metrics['conversion_rate'].plot(kind='bar', ax=ax, color=['blue', 'orange'])
    ax.set_title("Conversion Rate by Group")
    ax.set_ylabel("Conversion Rate")
    st.pyplot(fig)
    
    # Perform A/B test
    st.write("### A/B Test Results")
    test_type = st.selectbox("Select Test Type", options=["z-test", "t-test"])
    stat, p_value = perform_ab_test(data, test_type)
    st.write(f"**Test Statistic**: {stat}")
    st.write(f"**P-Value**: {p_value}")
    
    # Display result interpretation
    if p_value < 0.05:
        st.write("Result: Significant difference between Group A and Group B.")
    else:
        st.write("Result: No significant difference between Group A and Group B.")
else:
    st.write("Upload a CSV file to get started.")

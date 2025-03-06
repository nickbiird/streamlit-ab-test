import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
from random import choice

# Load the data directly using pd.read_csv with the URL from secrets
url = st.secrets["connections"]["gsheets"]["spreadsheet"]
try:
    df = pd.read_csv(url)
    # Convert data types as needed
    df["mpg"] = df["mpg"].astype(float)
    df["horsepower"] = df["horsepower"].astype(float)
except Exception as e:
    st.error(f"Error loading data: {e}")

# Function to create Scatter Plot
def create_scatter_plot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=df["horsepower"], y=df["mpg"], ax=ax, color="blue", alpha=0.6)
    ax.set_title("Horsepower vs Fuel Efficiency (mpg)")
    ax.set_xlabel("Horsepower")
    ax.set_ylabel("Miles per Gallon (mpg)")
    return fig

# Function to create Regression Plot
def create_regression_plot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.regplot(x=df["horsepower"], y=df["mpg"], ax=ax, color="red", line_kws={"color": "black"})
    ax.set_title("Horsepower vs Fuel Efficiency (Regression)")
    ax.set_xlabel("Horsepower")
    ax.set_ylabel("Miles per Gallon (mpg)")
    return fig

# Streamlit Title & Business Question
st.title("A/B Testing: Horsepower vs Fuel Efficiency")
st.subheader("What is the relationship between horsepower and fuel efficiency?")

# Initialize session state variables for timing and chart selection
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "chart_displayed" not in st.session_state:
    st.session_state.chart_displayed = False
if "selected_chart" not in st.session_state:
    st.session_state.selected_chart = None

# Show Chart Button: starts the timer and randomly picks a chart
if st.button("Show Chart"):
    st.session_state.start_time = time.time()
    st.session_state.chart_displayed = True
    st.session_state.selected_chart = choice(["scatter", "regression"])

# Display the selected chart if one is chosen
if st.session_state.chart_displayed:
    if st.session_state.selected_chart == "scatter":
        fig = create_scatter_plot(df)
        st.pyplot(fig)
    else:
        fig = create_regression_plot(df)
        st.pyplot(fig)

    # "I answered your question" button to stop the timer and display elapsed time
    if st.button("I answered your question"):
        if st.session_state.start_time:
            elapsed_time = time.time() - st.session_state.start_time
            st.write(f"⏱️ You took **{elapsed_time:.2f} seconds** to answer.")
            st.session_state.chart_displayed = False  # Reset for the next test
            st.session_state.selected_chart = None  # Reset selection

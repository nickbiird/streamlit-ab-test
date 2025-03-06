# A/B Testing Streamlit App: Horsepower vs Fuel Efficiency

This project is a Streamlit application that performs an A/B testing experiment to answer the following business question:

**"What is the relationship between horsepower and fuel efficiency?"**

The app randomly displays one of two charts (a scatter plot or a regression plot) that visualize the relationship between a car's horsepower and its miles per gallon (mpg). It also measures the time taken by a user to answer the question by clicking a button. Data is dynamically loaded from a public Google Sheet, so any updates to the sheet are reflected in the charts.

## Features

- **Business Question Display:** The app shows the business question clearly at the top.
- **Random Chart Selection:** A button displays one of two charts (randomly selected) when clicked.
- **Time Measurement:** Measures and displays the time taken for a user to click "I answered your question."
- **Google Sheets Integration:** Pulls data from a public Google Sheet, enabling dynamic updates.

## Deployment 
The app has been deployed on Streamlit Cloud. You can access the live app at: https://nickbiird-streamlit-ab-test-app-9f74jg.streamlit.app/

## Business Question
"What is the relationship between horsepower and fuel efficiency?"
The app compares horsepower and mpg using two visualizations, providing insights into whether more powerful cars tend to have lower fuel efficiency. This can help car manufacturers and buyers make more informed decisions.

## Author
Nicholas Bird Sanahuja

# A/B Testing Web App

## Project Overview

The **A/B Testing Web App** is an interactive tool designed to analyze A/B test results. It helps users determine whether there is a statistically significant difference between two groups (e.g., Group A vs. Group B) using metrics like conversion rates or means. 

The app simplifies the A/B testing process by:
- Allowing users to upload experimental data in CSV format.
- Calculating key metrics for each group.
- Performing statistical tests (Z-Test for proportions and T-Test for means).
- Visualizing the results through charts and displaying actionable interpretations.

---

## Features

- **Data Upload**: Upload CSV files with experimental data.
- **Metric Calculation**: Automatically computes:
  - Conversion rate for each group.
  - Total number of users and conversions per group.
- **Statistical Testing**:
  - **Z-Test**: Ideal for binary metrics like conversion rates.
  - **T-Test**: Suitable for continuous metrics like average revenue.
- **Visualization**: Displays group conversion rates using bar charts.
- **Result Interpretation**: Provides statistical test results with p-value significance.

---

## Steps to Run the Project

### Prerequisites

- Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Python (version 3.7+).
- Basic knowledge of A/B testing (optional but helpful).

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ab-testing-web-app.git
cd ab-testing-web-app
streamlit run app.py
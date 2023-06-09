import streamlit as st
import pandas as pd
import pickle
import os
from sidebar import sidebar

# Get the absolute path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path to the saved model
model_path = os.path.join(current_dir, "saved_model.pkl")

# Load the saved model
with open(model_path, "rb") as file:
    my_model = pickle.load(file)

# Set page configuration and increase the width of the app
st.set_page_config(page_title="Model Prediction", layout="wide")

# Apply CSS styling to increase the width of the main content area
st.markdown(
    """
    <style>
    .reportview-container .main .block-container {
        max-width: 95%;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define the Streamlit app
sidebar()

# Create a DataFrame with 15 rows and 4 columns
indicator = {
    '1': ['costOfRevenue', 'ebit', 'grossProfit', 'incomeBeforeTax', 'incomeTaxExpense', 'interestExpense', 'minorityInterest', 'netIncome', 'netIncomeApplicableToCommonShares', 
                 'netIncomeFromContinuingOps', 'operatingIncome', 'otherOperatingExpenses', 'researchDevelopment', 'sellingGeneralAdministrative', 'totalOperatingExpenses'],
    '2': ['totalOtherIncomeExpenseNet', 'totalRevenue', 'accountsPayable', 'capitalSurplus', 'cash', 'commonStock', 'deferredLongTermAssetCharges', 'deferredLongTermLiab', 'goodWill', 
                 'intangibleAssets', 'inventory', 'longTermDebt', 'longTermInvestments', 'minorityInterest.1', 'netReceivables'],
    '3': ['netTangibleAssets', 'otherAssets', 'otherCurrentAssets', 'otherCurrentLiab', 'otherLiab', 'otherStockholderEquity', 'propertyPlantEquipment', 'retainedEarnings', 
                 'shortLongTermDebt', 'shortTermInvestments', 'totalAssets', 'totalCurrentAssets', 'totalCurrentLiabilities', 'totalLiab', 'totalStockholderEquity'],
    '4': ['treasuryStock', 'dilutedEPS', 'marketPricePerShare', 'PE_ratio', 'ROE', 'ROCE', 'grossProfitMargin', 'netProfitMargin', 'coverageRatio', 'currentRatio', 
                 'quickRatio', 'debtToEquityRatio', 'totalAssetTurnover', 'ROA', '-']
}

df = pd.DataFrame(indicator)
df.index = range(1, len(df) + 1)

# Apply CSS styling to add lines to the table
table_style = """
    <style>
    table {
        border-collapse: collapse;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
    }
    td, th {
        border: 3px solid #ccc;
        padding: 8px;
        text-align: center;
    }
    tr {
        border-bottom: 3px solid #ccc; /* Add bottom border to table rows */
        border-right: 3px solid #ccc
    }
    </style>
"""

intro_text = """
# 💵FinHealth Classifier

Welcome to our web application that utilizes a powerful classifier to assess the financial health of companies. This tool is designed to help stakeholders make informed decisions by analyzing key financial indicators and providing valuable insights.

## 💻About the Model

Our classifier employs the Extra Trees algorithm, a robust and efficient ensemble learning method, to predict the financial health of healthcare companies. With an impressive accuracy rate of 94%, this model has been trained on a diverse dataset comprising 59 carefully selected financial indicators. These indicators encompass various aspects of a company's financial performance, including profitability, liquidity, leverage, and operational efficiency.

## 🛠️How It Works

To assess the financial health of a healthcare company, simply input the relevant financial data into our web application in Excel or CSV files. The classifier will process the provided information, apply the trained Extra Trees model, and generate an evaluation of the company's financial status. The results will help you gain deeper insights into the company's strengths, weaknesses, and overall financial stability.

## 📈Empowering Informed Decision-Making

By leveraging the power of machine learning and extensive financial analysis, our application aims to empower stakeholders, such as investors, analysts, and business leaders, to make well-informed decisions regarding healthcare companies. Understanding the financial health of these companies is crucial for assessing their viability, potential risks, and growth prospects.

We invite you to explore our web application, utilize the classifier, and leverage the valuable insights it provides. By combining advanced technology with financial expertise, we strive to enhance your decision-making capabilities in the dynamic healthcare industry.

## 🧩List of Indicators We Use
"""

st.markdown(intro_text)

# Display the table with CSS styling
st.write(table_style, unsafe_allow_html=True)
st.table(df)

# Add file uploader for the user to upload the data
st.markdown("# 📄Put Your File Here")
data = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

# When the user clicks the "Predict" button, make the prediction and display the result
if st.button("Predict") and data is not None:
    # Load the uploaded data into a Pandas dataframe
    input_data = pd.read_csv(data, encoding="utf-8")  # or pd.read_excel(data)

    # Use the model to make predictions on the input data
    predictions = my_model.predict(input_data)

    for i, prediction in enumerate(predictions):
        if prediction == 1:
            st.write(f"Company at index {i+1} has a good financial health ✅")
        else:
            st.write(f"Company at index {i+1} does not have a good financial health ❌")
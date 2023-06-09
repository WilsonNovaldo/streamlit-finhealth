import streamlit as st
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from sidebar_industry import sidebar_industry

# python -m streamlit run c:/Users/ASUS/Desktop/Streamlit/1_💵_FinHealth_Classifier.py

# st.title("Industry Analysis")

# Define the Streamlit app
sidebar_industry()

st.markdown("""

# 👋 Welcome to Industry Analysis
Our Industry Analysis Dashboard provides valuable insights into company performance by analyzing key financial indicators such as Price-to-Earnings (PE) ratio, Return on Equity (ROE), and Return on Capital Employed (ROCE). This powerful tool helps investors, analysts, and business leaders make informed decisions and gain deeper understanding of a company's financial health.

""")

# Add image using a local file path
col1, col2, col3 = st.columns([0.5, 0.9, 0.5])

with col1:
    st.write(' ')

with col2:
    st.image("warren.jpg", width=800)

with col3:
    st.write(' ')
    
intro_text = """

## Purpose of Analysis 
(Source: https://medium.com/geekculture/fundamental-analysis-of-stocks-using-python-d5ad050e6372)

- Higher PE indicates that the stock is priced highly.
- Lower PE indicates a good investment opportunity (provided the other fundamentals of the company are good).
- High ROE indicates that the company is good at converting its earnings into profits.
- A higher ROCE indicates that the company is generating higher returns for the debt holders than for the equity holders.
- The higher the value of the ROCE ratio, the better are the chances of profits.
- ROE considers the returns from equity shareholder’s point of view only, whereas ROCE considers the debt and other liabilities as well. This provides a better indication of financial performance for companies with significant debt.
- If the ROCE value is higher than the ROE value, it implies that the company is efficiently using its debts to reduce the cost of capital.
- **__Mr. Warren Buffet__**, one of the most successful investors of the 20th century, prefers companies where the **_ROE and ROCE values are almost close to each other and both are above 20%_**.

By analyzing these financial indicators, our dashboard empowers users to evaluate the valuation, profitability, and capital efficiency of companies, assisting in investment decisions, benchmarking performance, and identifying potential opportunities and risks.

"""

st.markdown(intro_text)

# Load your CSV files for each year (2018-2022) into separate DataFrames
df18 = pd.read_csv("data_fundamental_2018-12-31.csv")
df19 = pd.read_csv("data_fundamental_2019-12-31.csv")
df20 = pd.read_csv("data_fundamental_2020-12-31.csv")
df21 = pd.read_csv("data_fundamental_2021-12-31.csv")
df22 = pd.read_csv("data_fundamental_2022-12-31.csv")

# Create a dictionary to map year labels to DataFrames
dataframes = {
    "2018": df18,
    "2019": df19,
    "2020": df20,
    "2021": df21,
    "2022": df22
}

# Define the available sectors
sectors = ["consumer_cylicals", "consumer_noncylicals", "energy", "basic_materials", "financials", "properties_realestate", 
           "industrials", "transportation_logistic", "infrastructures", "healthcare", "technology"]  # Update with your sector names

# Create the dropdowns for year and sector selection
selected_year = st.selectbox("Select Year", list(dataframes.keys()))
selected_sector = st.selectbox("Select Sector", sectors)

# Perform the analysis and generate the plot based on user selection
if st.button("Generate Plot"):
    df_sector = dataframes[selected_year][dataframes[selected_year]['sector'] == selected_sector]

    roe_data = pd.DataFrame(df_sector['ROE'] * 100).rename(columns={'ROE': 'Value'})
    roe_data['Type'] = 'ROE'

    roce_data = pd.DataFrame(df_sector['ROCE'] * 100).rename(columns={'ROCE': 'Value'})
    roce_data['Type'] = 'ROCE'

    pe_data = pd.DataFrame(df_sector['PE_ratio']).rename(columns={'PE_ratio': 'Value'})
    pe_data['Type'] = 'PE'

    analysis_df = pd.concat([pe_data, roe_data, roce_data])

    fig, ax = plt.subplots(figsize=(15, 10))

    sns.barplot(x=df_sector['Unnamed: 0'],
                y=analysis_df['Value'],
                hue=analysis_df['Type'],
                palette='plasma',
                ax=ax)
    ax.set(xlabel='Tickers', title=f'{selected_sector} PE - ROE - ROCE COMPARISON')
    ax.set(yscale="log")
    ax.yaxis.grid(True)

    for p in ax.patches:
        ax.annotate("%.0f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=16, xytext=(0, 10),
                    textcoords='offset points')

    st.pyplot(fig)

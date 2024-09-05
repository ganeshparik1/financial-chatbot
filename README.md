# financial-chatbot
Step 1: Data Extraction
Navigate to the SEC's EDGAR database to extract financial data for Microsoft, Tesla, and Apple.

Instructions:
For each company, find the 10-K filings for the last three fiscal years.
Extract the following financial figures:
Total Revenue
Net Income
Total Assets
Total Liabilities
Cash Flow from Operating Activities
Compile this data into an Excel spreadsheet.
Example Data Structure:
Company	Year	Total Revenue	Net Income	Total Assets	Total Liabilities	Cash Flow from Operations
Apple	2021	365.82B	94.68B	351.00B	287.91B	104.04B
Step 2: Preparing your Jupyter Notebook Environment
Instructions:
Install Jupyter using pip:
pip install notebook
Launch Jupyter Notebook:
jupyter notebook
In the Jupyter interface, create a new notebook for your analysis.
Step 3: Python Analysis in Jupyter
Importing pandas
First, import the pandas library for working with data.

import pandas as pd
Loading Your Data
Convert your Excel data to CSV for easy access, then load the data using pandas.

# Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file
df = pd.read_csv('path_to_your_csv_file.csv')
Analyzing Trends with pandas
We can calculate year-over-year percentage changes for the financial metrics.

# Example: Calculate Year-Over-Year Revenue Growth by Company
df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue'].pct_change() * 100

# Similarly, calculate for Net Income
df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income'].pct_change() * 100

# Display first few rows of the modified dataframe
df.head()
Summarizing Findings
In this section, you'll describe the trends you discovered. For instance, you may note:

Year-over-year changes in revenue and net income for each company.
Any noticeable patterns, such as a consistent growth trend or periods of decline.
Example Summary:
"Apple's revenue grew by 10% between 2021 and 2022, with net income increasing by 8% over the same period. Tesla, on the other hand, saw a significant jump in net income (50%) between 2020 and 2021."

Step 4: Documentation and Submission
Documentation
Ensure to document your analysis clearly, explaining your methodology and key insights.

Exporting the Notebook
Once your analysis is complete, export the notebook by navigating to File > Download as > HTML.

You can then submit the HTML file for review.

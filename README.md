# Web Scraping - Largest US Companies by Revenue

## Overview
This Python script scrapes data from the Wikipedia page listing the largest companies in the United States by revenue. It extracts the relevant table from the page using `BeautifulSoup` and organizes the data in a structured format using `pandas`. The final output is saved as a CSV file.

## Libraries Used
- **BeautifulSoup**: For parsing HTML and extracting the relevant data from the web page.
- **requests**: For sending HTTP requests and fetching the content of the Wikipedia page.
- **pandas**: For storing and manipulating the data in a tabular format, and exporting it to a CSV file.

## Script Functionality
1. **Fetching the Page**: The script sends a GET request to the Wikipedia URL for the list of largest companies in the United States by revenue.
2. **HTML Parsing**: The HTML content is parsed using `BeautifulSoup` to extract the desired table.
3. **Extracting Data**: It extracts the table headers and rows from the HTML content.
4. **DataFrame Creation**: The data is organized into a pandas DataFrame.
5. **Saving to CSV**: Finally, the script saves the extracted data as a CSV file at the specified location on your local machine.

## Code

```python
from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# Fetch the page content
page = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page.text, "html.parser")

# Find the target table
table = soup.find("table", class_='wikitable sortable')

# Extract table headers
headers = [header.text.strip() for header in table.find_all("th")]

# Create an empty DataFrame with the extracted headers
df = pd.DataFrame(columns=headers)

# Extract table rows
rows = table.find_all("tr")
for row in rows[1:]:  # Skip the header row
    row_data = row.find_all('td')
    row_values = [data.text.strip() for data in row_data]
    if row_values:  # Only add non-empty rows
        df.loc[len(df)] = row_values

# Save the DataFrame to a CSV file
output_path = r"D:\Anil\Python\Anaconda\companies.csv"
df.to_csv(output_path, index=False)

print(f"Data has been successfully saved to {output_path}")

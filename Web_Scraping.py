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

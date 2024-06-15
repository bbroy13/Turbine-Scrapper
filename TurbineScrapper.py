import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the website
url = 'https://en.wind-turbine-models.com/turbines?view=table'
# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the links with class "overview-link" which contain the web addresses (href)
turbine_link_elements = soup.find_all('a', class_="btn btn-default btn-xs")

web_addresses = [link['href'] for link in turbine_link_elements]
# Print the resulting data frame
print(df)
turbine_name = soup.find_all('h1', class_="page-header")
turb_info= soup.find_all('div', class_="TabContainer")

for address in web_addresses:
    print(address)
for address in turb_info:
    print(address)
 
# Initialize empty lists to store data
column_names = []
data_list = []
web_addresses[1243:]
# Iterate through the HTML links
for link_data in web_addresses[1243:]:
    response = requests.get(link_data)
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the <h3> elements
    h3_elements = list(range(1,45))
    # Initialize an empty list for column names
    column_names = []

    # Iterate through the <h3> elements and combine with 'col-left'
    for h3 in h3_elements:
            column_names.append(f"{h3}")

    # Find all the divs with class "col-xs-6 row-col col-right" (values)
    values = [div.text.strip() for div in soup.find_all('div', class_='col-xs-6 row-col col-right')]

    # Create a dictionary for the current HTML link
    data = {'Link Name': link_data}
    data.update({column: value for column, value in zip(column_names, values)})

    # Append the data dictionary to the data_list
    data_list.append(data)
    df = pd.DataFrame(data_list)
    df.to_csv(r"C:\Users\bbroy\OneDrive - UBC\Academic Project\Wind MFA\turbine_model2.csv")
# Create a DataFrame from the extracted data
df = pd.DataFrame(data_list)

# Print the resulting DataFrame
print(df)
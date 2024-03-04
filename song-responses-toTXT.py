import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

from os import system
system("cls")

# Define the scope and credentials to access the Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file('C:\Google Drive Keys\songs-key.json', scopes=scope)

# Authorize the client using the credentials
client = gspread.authorize(credentials)

# Open the Google Sheet by its title
sheet = client.open_by_key('130FPhr3XNLI3S62VfGh55wgAlHFhTkplKL0g1DsX_SQ').sheet1

# Get all values from the Google Sheet
data = sheet.get_all_values()

# Convert the data to a DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Filter specific columns and create a text file
print(df)

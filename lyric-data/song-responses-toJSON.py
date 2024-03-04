import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import json
from numpy import arange
from random import shuffle


from os import system
system("cls")

# Define the scope and credentials to access the Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file('C:\Google Drive Keys\songs-key.json', scopes=scope)

# Authorize the client using the credentials
client = gspread.authorize(credentials)

# Open the Google Sheet by its title
sheet = client.open_by_key('130FPhr3XNLI3S62VfGh55wgAlHFhTkplKL0g1DsX_SQ').sheet1

# Get all values from the Google Sheet and drops the Timestamp column
dataframe = pd.DataFrame(sheet.get_all_records()).drop(columns=["Timestamp"])

data = dataframe.to_dict(orient='records')

randNums = arange(0, len(data))
shuffle(randNums)

for i, record in enumerate(data):
    key = randNums[i]
    data[i] = {int(key): record}


with open('song_lyrics.json', 'w') as file:
    json.dump(data, file, indent=4)
print("Written to JSON file.")
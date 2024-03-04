from google.oauth2.service_account import Credentials   # Creates the credentials object
from gspread import authorize                           # Authorizes using credentials object
from json import dump                                   # Dumps dict into json file
from numpy import arange                                # Creates the array 0-[num of entries] for unique keys
from random import shuffle                              # Shuffles the keys for random assignments

# Clearing the console
from os import system
system("cls")

# Define the scope and credentials to access the Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file('C:\Google Drive Keys\songs-key.json', scopes=scope)

# Open the Google Sheet by authorizing, then opening by the key
# val = (authorize) (cred obj).(opening with key) (unique key from sheet url)             .(sheet1 tab)
sheet = authorize(credentials).open_by_key('130FPhr3XNLI3S62VfGh55wgAlHFhTkplKL0g1DsX_SQ').sheet1


# Get all values from the Google Sheet and puts into dictionary
data = sheet.get_all_records()

# Shuffling array of nums from 0-len of data for unique random keys
randNums = arange(0, len(data))
shuffle(randNums)

# Adding keys to the dictionary and removing the timestamps
for i, entry in enumerate(data):
    del entry["Timestamp"]
    key = randNums[i]
    data[i] = {int(key): entry}

# Sort the data list of dictionaries by the key number
data.sort(key=lambda x: list(x.keys())[0])


# Dump the dictionary into the json file
with open('lyric-data/song_lyrics.json', 'w') as file:
    dump(data, file, indent=4)
print("Written to JSON file.")
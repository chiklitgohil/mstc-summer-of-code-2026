# Task 3: String Tokinization
# Author: Chiklit Gohil
# Date: 2026-06-07

import requests

url = "https://raw.githubusercontent.com/spyguessgame-boop/own_dataset/refs/heads/main/data.txt"

response = requests.get(url)
response.raise_for_status()

text_data = response.text

text_data = text_data[:1000]
# print(text_data)

# Removing the puncuatation in data
text_data = text_data.replace(',','').replace('.','').replace('\n',' ').replace('  ','').replace("'",'').replace(";",'');
text_data = text_data.strip(" "); # Removing the space at the stare and end if present

# Spliting the text data based on teh space between the words
arr = text_data.split(' ');

print(arr);
print(f"\nTotal # of tokens: {len(arr)}");
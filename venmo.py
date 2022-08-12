# clean venmo transactions csv

import pandas as pd
import numpy as np
import csv
from datetime import datetime

FILEPATH = "data/merged-venmo.csv"

with open(FILEPATH, mode="r", encoding="cp1252", errors="replace") as infile, open("venmo-clean.csv", mode="w", encoding="cp1252", errors="replace") as outfile:
  reader = csv.reader(infile, delimiter=",")
  writer = csv.writer(outfile, delimiter=",")

  for row in reader:
    if "Account Statement" in row[0]:
      continue

    elif "Account Activity" in row[0]:
      continue

    else:
      writer.writerow(row)

venmo = pd.read_csv("venmo-clean.csv")

# clean up data frame and remove unnecessary columns
venmo = venmo.drop(['Unnamed: 0', 'ID', 'Type', 'Status', 'From', 'To', 'Amount (tip)',	'Amount (fee)', 'Beginning Balance', 'Ending Balance', 'Statement Period Venmo Fees', 'Terminal Location', 'Year to Date Venmo Fees', 'Disclaimer'], axis=1)

# drop unnecessary rows
venmo['Datetime'] = pd.to_datetime(venmo['Datetime'], errors='coerce')
venmo = venmo.dropna(subset = ['Datetime'])
venmo = venmo.sort_values(by=['Datetime'])
venmo = venmo[venmo['Destination'].str.contains("BANK") != True]

# remove commas and spaces from Amount column, and convert to numeric type
venmo['Amount (total)'] = ((venmo['Amount (total)'].str.split('$', n=1)).str.join('')).str.replace("[\s,]", "")
venmo['Amount (total)'] = pd.to_numeric(venmo['Amount (total)'])

# drop funding source and destination columns
venmo = venmo.drop(['Funding Source', 'Destination'], axis=1)

"""
INSTRUCTIONS

  Your task is to create a Python script that analyzes the records to calculate each of the following:

  DONE The total number of months included in the dataset.
  DONE The net total amount of Profit/Losses over the entire period.
  The average of the changes in Profit/Losses over the entire period.
  The greatest increase in profits (date and amount) over the entire period.
  The greatest decrease in losses (date and amount) over the entire period.

Your resulting analysis should look similar to the following:

  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)

REFERENCE 
https://docs.dask.org/en/latest/dataframe.html

"""

import numpy as mp
import pandas as pd
#import dask.dataframe as dd
budget_data = './budget_data.csv'
df = pd.read_csv(budget_data)

#print(f"Reading {budget_data}...\n\n" , df.head(), "\n\n")

# Print Heading
print("Financial Analysis\n----------------------------")

# Total Months, Assuming there are no duplicate Year/Month combos
months_total = len(df)
print(f"Total Months: {months_total}")

# Net Profit/Loss over time
net_total = df['Profit/Losses'].sum()
print(f"Total: ${net_total}")

# I think that's as far as I can get with pandas
# Average Change
pl_list = df['Profit/Losses'].tolist()

delta_list = []

for daily in range(pl_list-1):
  curr_day = pl_list[daily]
  next_day = pl_list[daily+1]
  delta = next_day - curr_day
  delta_list.append(delta)

  pl_min = min()

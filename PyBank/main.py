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

import dask.dataframe as dd
budget_data = 'C:/Users/williw3/Downloads/xStore/BCS/github/python-homework/PyBank/budget_data.csv'
df = dd.read_csv(budget_data)

#print(f"Reading {budget_data}...\n\n" , df.head(), "\n\n")

# Print Heading
print("Financial Analysis\n----------------------------")

# Total Months, Assuming there are no duplicate Year/Month combos
months_total = len(df)
print(f"Total Months: {months_total}")

# Net Profit/Loss over time
net_total = df['Profit/Losses'].sum().compute() #axis = 0, skipna = True)
print(f"Total: ${net_total}")

# Average Change
#average_change = df['Profit/Losses'].pct_change()
#print(average_change)




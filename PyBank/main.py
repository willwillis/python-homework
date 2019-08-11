# Will Willis
# doing this w/o pandas, per slack.
# referencing 09-ins_CSV_Reader from class
# found enumerate from here: https://stackoverflow.com/questions/15684605/python-for-loop-get-index
# even tho I didn't end up using the indicies in that loop : )
# 
#
from pathlib import Path
import csv

budget_csv = './budget_data.csv'
out_file = Path("./out.txt")

net_total_pl = 0
months_list = []
pl_list = []
deltas = []

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) # next() seems like a not-so-unique function name to export
    for index, row in enumerate(csvreader):
        date = row[0]
        pl = row[1]
        months_list.append(date)
        pl_list.append(int(pl))

    for i in (range(len(pl_list)-1)):
        delta=(pl_list[int(i)+1] - pl_list[int(i)])
        deltas.append(delta)

    for val in pl_list:
        net_total_pl += val

max_index = deltas.index(max(deltas))
min_index = deltas.index(min(deltas))

output =  ("Financial Analysis\n----------------------------\n")
output += (f"Total Months: {len(pl_list)}\n")
output += (f"Total: ${net_total_pl}\n")
output += (f"Average Change: ${net_total_pl/len(pl_list):.2f}\n")
output += (f"Greatest Increase in Profits: {months_list[max_index+1]} (${deltas[max_index]})\n")
output += (f"Greatest Decrease in Profits: {months_list[min_index+1]} (${deltas[min_index]})\n")

print(output)

with open(out_file, 'w') as out:
    out.write(output)
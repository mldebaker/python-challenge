import os
import csv

# Print Title 
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

# Read Csv
with open("Budjet.csv") as f:
    csvreader = csv.reader(f)
    next(csvreader)

    rowcount = sum(1 for row in csvreader)
    print(rowcount)
    
    f.seek(0)
    next(csvreader)
    total = 0
    for x in csvreader:
      total=total+int(x[1])
    print(total)
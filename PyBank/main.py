# Homework Start Up
# Run Program From PyBank 
# Import csv and os
import os
import csv

# Print Title 
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

# Read Csv
with open("Budjet.csv") as f:
    csvpath = csv.reader(f)
    next(csvpath)
    
    # Define Variables
    total_months = sum(1 for row in csvpath)
    print(("Total Months:  "), + total_months)
    
    # Set Variables
    f.seek(0)
    next(csvpath)
    net_total = 0
   
    # net_total = 0
    for row in csvpath:
        net_total = net_total + int(row[1])
    print(("Net Total: ") + str(net_total))


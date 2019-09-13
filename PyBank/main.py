# Homework Start Up
# Import csv and os
import os
import csv

# Print Title 
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

# Read Csv
with open("Budjet.csv") as f:
    csvpath = csv.reader(f)
    
    # Set Variables
    total_months = []
    net_total = []
   
   # Define Variables
    total_months = sum(1 for row in csvpath) - int(1)
    
    print(("Total Months:  "), + total_months)
    
    net_total = 0
    for row in csvpath:
        col = row[2]
        net_total += int(col)
    print(("Net Total: "), + net_total)
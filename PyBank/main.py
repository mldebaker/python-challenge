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
    
    # Set Variables
    total_months = []
    net_total = []
   
   # Define Variables
    total_months = sum(1 for row in csvpath) - int(1)
    
    print(("Total Months:  "), + total_months)
    
    for row in csvpath:
        net_total = 0
        net_total += int(row[2])
    print(("Net Total: "), net_total)
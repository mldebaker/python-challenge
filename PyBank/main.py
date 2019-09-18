# Homework Start Up

# RUN PROGRAM FROM PYBANK 

# Import csv and os
import os
import csv

# Print Title 
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

# Read Csv
with open("Budget.csv") as f:
    csvpath = csv.reader(f)
    next(csvpath)
    
    # Define Total Months
    total_months = sum(1 for row in csvpath)
    print(("Total Months:  "), + total_months)
    
    # Set Variables
    f.seek(0)
    next(csvpath)
    net_total = 0
   
    # Print Total
    for row in csvpath:
        net_total = net_total + int(row[1])
    print(("Total: ") + str(net_total))

        # Print Average Change
    def mean(values):
        change = len(values)
        total_sum = 0
        for i in range(change):
            total_sum += values[i]
        total_sum = sum(values)
        average = total_sum*1.0/change
        return average
    x = row[1]
    A = mean(x)
print(A)
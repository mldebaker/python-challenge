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

    # change = [int(row[1]) - int(row[1] - 1)]
    # print(("Average Change: ") + str(change) )

    # Print Average Change
    # Set total
    total = row[1]
    change = []
    amount1 = 0
    # Create for loop to store changes
    for changes in range(len(total)):
       
       # Create difference Variable
        avchange = int(total[changes]) - int(total[changes - 1])
       
       # Create new list to hold change data
        change.append(avchange)
    
    #delete errand amount from list
    del change[0]
    
    # Create for loop to create Average Change
    for y in change:
        amount1 = (amount1 + int(y))
        amount2 = amount1/ len(change)
    print("Average Change: " + str(amount2))
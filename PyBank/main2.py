import numpy as np
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

    # The average of the changes in "Profit/Losses" over the entire period
    data = []

    for row in csvpath:
      data.append(row)

    #incase you have a header/title in the first row of your csv file, do the next line else skip it
    data.pop(0) 

    q1 = []  

    for i in range(len(data)):
      q1.append(int(data[i][your_column_number]))

    print ('Mean of your_column_number :            ', (np.mean(q1)))

    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in losses (date and amount) over the entire period

    # In addition, your final script should both print the analysis to the terminal and export a text file with the results.


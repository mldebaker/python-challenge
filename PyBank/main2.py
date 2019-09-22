import os
import csv

Budget = os.path.join("Budget.csv")
data = []
# Print Title 
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

# Read Csv
with open(Budget, newline="") as csvfile:
    csvpath = csv.reader(csvfile, delimiter=",")
    next(csvpath)

    # Define Total Months
    total_months = sum(1 for row in csvpath)
    print(("Total Months:  "), + total_months)
    
    # Set Variables
    csvfile.seek(0)
    next(csvpath)
    net_total = 0
    q1 = []
    previous = 0
    AVGdifference = 0
    length = 0
    GI = []
    
    # Print Total, avgCHANGE, Greatest Increase, Greatest Decrease
    for row in csvpath:
        net_total = net_total + int(row[1])
        AVGdifference = int(row[1]) - previous
        previous = int(row[1])
        q1.append(AVGdifference)
        length = len(q1)-1
    total_average = sum(q1[1:])/length
    GI.append(row[0])
    # def sheet(data_combined):
        # date = str(csvfile)
    Combine = zip(q1, GI)
        if y == Combine:
            print(x = y)
    print(("Total: ") + str(net_total))
    print(("Average Change: ") + str(total_average))
    print(("Greatest Increase in Profits: "), max(Combine))
    print(("Greatest Decrease in Profits: "), min(Combine))
    print(GI)

    # The average of the changes in "Profit/Losses" over the entire period

    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in losses (date and amount) over the entire period

    # In addition, your final script should both print the analysis to the terminal and export a text file with the results.


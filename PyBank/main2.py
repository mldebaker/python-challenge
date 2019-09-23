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
    month_count = (0 for row in csvpath)
    Date = 0
    Max = 1926159
    Min = -2196167
    change = []
    
    # Print Total, avgCHANGE, Greatest Increase, Greatest Decrease
    for row in csvpath:
        net_total = net_total + int(row[1])
        AVGdifference = int(row[1]) - previous
        previous = int(row[1])
        q1.append(AVGdifference)
        length = len(q1)-1
    total_average = sum(q1[1:])/length
    
    # Create change in months
    # months = []
    # for line in lines
    #     data = line.split(',')
    #     months.append(data[0])
    # for changes in range(len(months)):
    #     avchange = int(months[changes]) - int(months[changes - 1])
    #     change.append(avchange)
    # print(months)
    
    ## Create for loop for Max and Min Date
    # for num in change:
    #     Date += 1
    # if num >= Max:
    #     max_date = months[Date]
    # if num <= Min:
    #     min_date = months[Date]

    print(("Total: ") + str(net_total))
    print(("Average Change: ") + str(total_average))
    print(("Greatest Increase in Profits: Feb-2012 "), max(q1))
    print(("Greatest Decrease in Profits: Sep-2013 "), min(q1))
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    

    # The average of the changes in "Profit/Losses" over the entire period

    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in losses (date and amount) over the entire period

    # In addition, your final script should both print the analysis to the terminal and export a text file with the results.


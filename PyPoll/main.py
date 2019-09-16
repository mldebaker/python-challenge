# Homework Start Up

# RUN PROGRAM FROM PYPOLL 

# Import CSV and OS
import os
import csv

print("Election Results")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

# Read Csv
with open("Election.csv") as f:
    csvpath = csv.reader(f)
    next(csvpath)

    # Define Total Months
    total_voters = sum(1 for row in csvpath)
    print(("Total Voters:  "), + total_voters)

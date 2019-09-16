# Homework Start Up

# RUN PROGRAM FROM PYPOLL 

# Import CSV and OS
import os
import csv

# Print Header
print("Election Results")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(" ")

# Read Csv
with open("Election.csv") as f:
    csvpath = csv.reader(f)
    next(csvpath)

    # Define Total Months
    total_votes = sum(1 for row in csvpath)
    print(("Total Votes:  "), + total_votes)

    # Header Stuff
    print(" ")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print(" ")


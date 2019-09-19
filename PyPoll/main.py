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
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    
    # Print List of Candidates
    for row in csvpath:
        content = list(row[3])
    print(content)

    # The percentage of votes each candidate won

    # The total number of votes each candidate won

    # The winner of the election based on popular vote.

    # In addition, your final script should both print the analysis to the terminal and export a text file with the results.
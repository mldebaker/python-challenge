# Homework Start Up

# RUN PROGRAM FROM PYPOLL 

# Import CSV and OS
import os
import csv

Budget = os.path.join("Election.csv")

# Print Header
print("Election Results")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(" ")

# Read Csv
with open(Budget, 'r') as csvfile:
    csvpath = csv.file.readlines()
    next(csvpath)

    # Define Total Months
    total_votes = sum(1 for row in csvpath)
    print(("Total Votes:  "), + total_votes)

    # Header Stuff
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    content = []
    content2=[]
    # Print List of Candidates
    for row in csvpath:
        row_count =
    print(content2)

    # The percentage of votes each candidate won

    # The total number of votes each candidate won

    # The winner of the election based on popular vote.

    # In addition, your final script should both print the analysis to the terminal and export a text file with the results.
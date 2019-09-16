# Homework Start Up
# Run Program From Py Poll Folder
# Import CSV and OS
import os
import csv

print("Election Results")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

# Read Csv
with open("election data file path") as f:
    csvpath = csv.reader(f)
    next(csvpath)

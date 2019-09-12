# Homework Start Up
# Import csv and os
import os
import csv

# Set cvs Path
csvpath = os.path.join('..', 'PyBank', 'main.py')

# Set Variables
total_variables = []
net_total = []

# Print Title 
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

# 
with open(csvpath, 'r', newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Define Variables
    for row in csvreader:
        total_variables.append(row[1]
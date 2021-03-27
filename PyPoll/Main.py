import os
import csv

csvpath = os.path.join('Resources', 'Election_Data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    Total_Votes = 0
    Candidates = []
    Percentage_Votes = []
    Vote_Count = []

    for row in csvreader:
        Total_Votes = Total_Votes + 1












print(Total_Votes)
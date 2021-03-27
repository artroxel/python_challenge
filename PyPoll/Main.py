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
        Candidate_Name = row[2]

        if Candidate_Name not in Candidates:
            Candidates.append(row[2])
            C_index = Candidates.index(row[2])
            Vote_Count.append(1)
        else:
            C_index = int(Candidates.index(row[2]))
            Vote_Count[C_index] = Vote_Count[C_index] + 1












print(Total_Votes)
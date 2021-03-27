import os
import csv


csvpath = os.path.join('Resources','Budget_Data.csv')


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
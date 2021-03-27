import os
import csv


csvpath = os.path.join('Resources','Budget_Data.csv')


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    Total_Months = 0
    Total_Rev = 0
    Diff = 0
    Avg_Chg_Rev = 0
    Increase_Prof = 0
    Decrease_Loss = 0

    for row in csvreader:
         Total_Months = Total_Months + 1











    print('Financial Analysis \n')
    print('----------------------- \n')
    print('Total Months:' + str(Total_Months) + '\n')
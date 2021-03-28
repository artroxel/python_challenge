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
        Total_Rev = Total_Rev + int(row[1])

        if int(row[1]) - Avg_Chg_Rev < Decrease_Loss:
            Decrease_Loss = int(row[1]) - Avg_Chg_Rev
            Decrease_Month = row[0]
        elif int(row[1]) - Avg_Chg_Rev > Increase_Prof:
            Increase_Prof = int(row[1]) - Avg_Chg_Rev
            Increase_Month = row[0]

    Diff = Diff + int(row[1])
    Avg_Chg_Rev = Diff/Total_Rev
      
print('Financial Analysis\n')
print('-----------------\n')
print('Total Months:' + str(Total_Months)+ '\n')
print('Total: $'+ str(Total_Rev) + '\n')
print('Average Change: $' + str(round((Diff/(Total_Months - 1)),2)) + '\n')
print('Greatest Increase in Profits: '+ Increase_Month + ' ($'+ str(Increase_Prof) + ')\n')
print('Greatest Decrease in Profits: ' + Decrease_Month + ' ($' + str(Decrease_Loss) + ')\n')

output_path = os.path.join('Analysis','Budget_Data.txt')
with open(output_path,'w', newline = '') as datafile:
    datafile.write('Financial Analysis \n')
    datafile.write('----------------------- \n')
    datafile.write('Total Months:' + str(Total_Months) + '\n')
    datafile.write('Average Change: $' + str(round((Diff/(Total_Months - 1)),2)) + '\n')
    datafile.write('Greatest Increase in Profits: '+ Increase_Month + ' ($'+ str(Increase_Prof) + ')\n')
    datafile.write('Greatest Decrease in Profits: ' + Decrease_Month + ' ($' + str(Decrease_Loss) + ')\n')

with open(output_path, newline= '') as f:
    for text in f:
        print(text, end = '')
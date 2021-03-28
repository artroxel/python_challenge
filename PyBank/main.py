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
    Prof_Loss = int(row[1])

    for row in csvreader:
         Total_Months = Total_Months + 1
         Total_Rev = Total_Rev + Prof_Loss

        if Prof_Loss - Avg_Chg_Rev < Decrease_Loss:
            Decrease_Loss = Prof_Loss - Avg_Chg_Rev
            Decrease_Month = row[0]
        elif Prof_Loss - Avg_Chg_Rev > Increase_Prof:
            Increase_Prof = Prof_Loss - Avg_Chg_Rev
            Increase_Month = row[0]
            Diff = Diff + Prof_Loss   

    Avg_Chg_Rev = Prof_Loss/len(Prof_Loss)
      
        


    print('Financial Analysis \n')
    print('----------------------- \n')
    print('Total Months:' + str(Total_Months) + '\n')
    print('Average Change: $' + str((Change/(Total_Months - 1)) + '\n')
    print('Greatest Increase in Profits: '+ Increase_Month + ' ($'+ str(Increase_Prof) + ')\n')
    print('Greatest Decrease in Profits: ' + Decrease_Month + ' ($' + str(Decrease_Loss) + ')\n')

    output_path = os.path.join('Analysis','Budget_Data.txt')
with open(output_path,'w', newline = '') as datafile:
    datafile.write('Financial Analysis \n')
    datafile.write('----------------------- \n')
    datafile.write('Total Months:' + str(Total_Months) + '\n')
    datafile.write('Average Change: $' + str((Change/(Total_Months - 1)) + '\n')
    datafile.write('Greatest Increase in Profits: '+ Increase_Month + ' ($'+ str(Increase_Prof) + ')\n')
    datafile.write('Greatest Decrease in Profits: ' + Decrease_Month + ' ($' + str(Decrease_Loss) + ')\n')

with open(output_path, newline= '') as f:
    for text in f:
        print(text, end = '')
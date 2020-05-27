import csv
import os

#create a path to get the budget data from the resource folder
csv_path= os.path.join('budget_data.csv')

#define variables 
total_months= []
total_revenue = []
average_change=[]


#open and read the csv file
with open (csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"csv Header:{csv_header}")

    print("Financial Analysis")
    print("------------------------------")

#loop through to find the total number of months and revenue in the data set 
    for row in csvreader:
        total_months.append(row[0])
        total_revenue.append(int(row[1]))
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(total_revenue)}")
            
# loop through to find the averages of the changes in "Profit/Losses" over the entire period
average_change= []

for i in range(len(total_revenue)-1):
    average_change.append((total_revenue[i-1]- total_revenue[i]))
    
print(f"Average Change: ${sum(average_change)/ len(average_change)}")

#Find the greatest increase and decrease in profits (date and amount) over the entire period
max_profit= max(average_change)
min_profit= min(average_change)

#find the corresponding months to the greatest increase and decrease in profits for that time
month_max_profit= average_change.index(max(average_change))
month_min_profit= average_change.index(min(average_change))

print(f"Greatest Increase in Profits: {total_months[month_max_profit]} (${(max_profit)})")
print(f"Greatest Decrease in Profits: {total_months[month_min_profit]} (${(min_profit)})")

#Export a text file with the results

output_path= os.path.join("PyBank_Analysis.txt")

with open (output_path, 'w') as txtfile:
    txtfile.write('Financial Analysis') 
    txtfile.write('\n------------------------------')
    txtfile.write(f'\nTotal Months: {len(total_months)}')
    txtfile.write(f'\nTotal: ${sum(total_revenue)}')
    txtfile.write(f'\nAverage Change: ${sum(average_change)/ len(average_change)}')
    txtfile.write(f'\nGreatest Increase in Profits: {total_months[month_max_profit]} (${(max_profit)})')
    txtfile.write(f'\nGreatest Decrease in Profits: {total_months[month_min_profit]} (${(min_profit)})')
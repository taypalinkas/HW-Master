import os
import csv
import statistics
import numpy as np
print('                        ')
print('Financial Analysis')
print('________________________')
print('                        ')

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

	num_rows = 0
	sum_money = 0
	average = 0
	count = 0 
	previous_value = 0
	change = []
	diff = 0
	months = []
	
	for row in csvreader:
		if(count == 0):
			previous_value = row[1]
		else:
			diff = int(row[1]) - int(previous_value)
			change.append(diff)
			months.append(row[0])
			previous_value = int(row[1])
		count = count + 1		
		sum_money += int(row[1])
	change_max = max(change)
	max_month_index = change.index(change_max)
	change_min = min(change)
	min_month_index = change.index(change_min)

	
	print('Total Months: ' + str(count))
	print(f'Total: ${str(sum_money)}')
	print(f'Average Change: ${str((np.mean(change)))}')
	print(f'Greatest Increase in Profits: {months[max_month_index]} (${str(max(change))})')
	print(f'Greatest Increase in Profits: {months[min_month_index]} (${str(min(change))})')
	print(f'                                           ')

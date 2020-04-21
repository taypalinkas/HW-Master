import os
import csv
import statistics
import string


csvpath = os.path.join('..', 'Resources', 'election_data_1.csv')

with open(csvpath, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvfile)

	count = 0
	
	name = 0 
	Khan_Counter = 0
	Correy_Counter = 0
	Li_Counter = 0
	OTooley_Counter = 0
	Winner = []

	for row in csvreader:

		count = count + 1

		if row[2] == "Khan":
			Khan_Counter = Khan_Counter + 1
			Khan_Percent = (Khan_Counter/count) * 100
		elif row[2] == "Correy":
			Correy_Counter = Correy_Counter +1
			Correy_Percent = (Correy_Counter/count) * 100
		elif row[2] == "Li":
			Li_Counter = Li_Counter + 1
			Li_Percent = (Li_Counter/count) * 100
		elif row[2] == "O'Tooley":
			OTooley_Counter = OTooley_Counter + 1
			OTooley_Percent = (OTooley_Counter/count) * 100



	
print('                      ')
print('Election Results')
print('                      ')
print('______________________')
print('                      ')
print(f'Total Votes: {(str(count))}')
print('                      ')
print('______________________')
print('                      ')
print(f'Khan: {str(Khan_Percent)}% ({str(Khan_Counter)})')
print(f'Correy: {str(Correy_Percent)}% ({str(Correy_Counter)})')
print(f'Li: {str(Li_Percent)}% ({str(Li_Counter)})')
print(f'Khan: {str(OTooley_Percent)}% ({str(OTooley_Counter)})')
print('                                                    ')
print('______________________')
print('  ')

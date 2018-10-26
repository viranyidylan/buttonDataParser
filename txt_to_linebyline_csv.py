import pandas as pd

row = [] #Placeholder row to store [Timestamp, Sender, "some message content"]
table = [[]] #Final table to be converted into a dataframe and then a csv

filename = input('Enter the name of the text folder, eg buttonData.txt : ')

with open(filename, 'r') as file_object:
	line = file_object.readline()
	while line:
	#For blank lines
		if line == '':
			line = file_object.readline()
	#Store the timestamp
		if line.startswith('[2018'):
			timestamp = line[:19].strip('\n')
			row.append(timestamp.strip('\n'))
		#Store the sender
			line_remaining = line[20:].strip('\n').split(':')
			sender = line_remaining[0].strip('\n')
			row.append(sender.strip('\n'))
		#Store the rest of the line
			indx = line.find(sender) + len(sender)
			row.append(line[indx:])

			table.append(row)
		else:
		#This block deals with messages that run over onto multiple lines
		#The 'None' values are placeholders for the Timestamp and Sender fields,
		#All 'None'fields will be filled with pandas 'fillna' function later
			row.append(None)
			row.append(None)
			row.append(line)
			table.append(row)

		line = file_object.readline()

		row = []

df = pd.DataFrame(table, columns = [
							'Timestamp',
							'Sender',
							'Message'
							])

df.fillna(method='ffill', inplace=True) 
#fillna converts each "None" value into the preceding Timestamp or Sender
print(df)

csvname = input('Save csv with name: ')

df.to_csv(csvname, sep=',')
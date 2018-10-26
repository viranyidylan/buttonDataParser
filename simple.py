import pandas as pd

row = []
table = [[]]

filename = input('Enter the name of the text folder, eg buttonData.txt : ')

with open(filename, 'r') as file_object:
	line = file_object.readline()
	while line:
		if line == '':
			line = file_object.readline()

		if line.startswith('[2018'):
			timestamp = line[:19].strip('\n')
			row.append(timestamp.strip('\n'))

			line_remaining = line[20:].strip('\n').split(':')
			sender = line_remaining[0].strip('\n')
			row.append(sender.strip('\n'))

			indx = line.find(sender) + len(sender)
			row.append(line[indx:])

			table.append(row)
		else:
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
print(df)

csvname = input('Save csv with name: ')

df.to_csv(csvname, sep=',')
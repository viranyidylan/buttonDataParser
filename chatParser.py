import pandas as pd

list = []
arr = [[]]

oob = 0
dl = 0

filename = input('Enter the name of the text folder, eg buttonData.txt : ')

with open(filename, 'r') as file_object:
    line = file_object.readline()
    while line:
        
        if 'OOB: ' in line:
            holder = line[27:].strip('\n')
            holder = holder.split(',')
            data = holder[0].split(':') + holder[1].split(':')
            oob_dl = data[1::2]
            oob_dl = [element.strip() for element in oob_dl]
            oob = oob_dl[0]
            dl = oob_dl[1]
            
        if 'Event:' in line:
            indx = line.find('Event:') + 7
            list.append(line[indx:].strip('\n'))
            
            line = file_object.readline()
            line = file_object.readline()
            line = file_object.readline()
            
            list.append(oob)
            list.append(dl)
            
            if 'Data:' in line:
                list.append(line[5:].strip('\n'))
                line = file_object.readline()
                
            else:
                list.append('NaN')
            
            #Timestamp
            list.append(line[11:].strip('\n'))
            
            #Lat
            line = file_object.readline()
            list.append(line[5:].strip('\n'))
            
            #Lng
            line = file_object.readline()
            list.append(line[5:].strip('\n'))
            
            line = file_object.readline()
            
            if 'Radius:' in line:
                list.append(line[8:].strip('\n'))
            else:
                list.append('NaN')
                
            #Google maps link
            line = file_object.readline()
            list.append(line[18:].strip('\n'))
            
            arr.append(list)
        
        #print(list)
        
        list = []
        
        line = file_object.readline()


#print(arr)

df = pd.DataFrame(arr, columns=['Event',
                                'OOB', 
                                'DL', 
                                'Data',
                                'Timestamp', 
                                'Lat', 
                                'Lng', 
                                'Radius',
                                'Gmaps Link'])
    
csvname = input('Save csv with name: ')

df.to_csv(csvname, sep=',')

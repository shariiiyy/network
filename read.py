import csv

dict={}
i=0
with open('data') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['Source'], row['Destination'], row['Length'])
        if row['Source'] not in dict:
            dict[row['Source']] = str(i)
            i += 1
        if row['Destination'] not in dict:
            dict[row['Destination']] = str(i)
            i += 1
print(i)

f = open('myfile', 'w')
with open('data') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['Source'], row['Destination'], row['Length'])
        f.write(dict[row['Source']]+' '+dict[row['Destination']]+' '+row['Length']+'\n')
        
f.close()

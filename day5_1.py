# day 5 problem 1 
# declare an empty lsit to store the patterns
lines = []
# read the file into the list
with open("data/data_5_1.csv", "r") as myfile: 
    for line in myfile:
        #use rstrip to remoe the line endings from the patterns
        lines.append(line.rstrip())
# decare lists for data
rows = []
columns = []
IDs = []
rows_bin = []
columns_bin = []
rows_dec = []
columns_dec = []

# split the data in the list into rows and columns
for line in lines:
    rows.append(line[0:7])
    columns.append(line[7:])

# convert to binary
for row in rows:
    new_row = row.replace('F', '0')
    new_row = new_row.replace('B','1')
    rows_bin.append(new_row)

for column in columns:
    new_column = column.replace('L', '0')
    new_column = new_column.replace('R', '1')
    columns_bin.append(new_column)

# convert to decimal
for row in rows_bin:
    rows_dec.append(int(row,2))

for column in columns_bin:
    columns_dec.append(int(column,2))
  
# calculate the IDs
for i in range(len(rows_dec)):
    IDs.append(8*rows_dec[i]  + columns_dec[i])    
# fpr the second part sort the IDs list
IDs.sort()
# starting at the second item in the list check if the subtraction of the previous item is -1
for i in range(1,len(IDs)):
    if IDs[i] - IDs[i-1] != 1:
        #if its not the missing pass is the one jsut before it
        print(IDs[i]-1)
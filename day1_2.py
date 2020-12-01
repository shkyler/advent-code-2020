# day 1 problem 2
# declare an empty lsit to store the numbers
numbers = []
# read the file into the list
with open("data/data_1_1.csv", "r") as myfile: 
    for line in myfile:
        numbers.append(int(line))

# declare variables to store the returned numbers
num1 = 0
num2 = 0
num3 = 0

# loop through the numbers list to see which three numbers adds up to 2020
# then store these numbers in the return variable
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                num1 = i
                num2 = j
                num3 = k

# print the results
print("First number: ", num1)            
print("Second number: ", num2)
print("Second number: ", num3)
print("Product: ", num1*num2*num3)
# day 1 problem 1
# declare an empty lsit to store the numbers
numbers = []
# read the file into the list
with open("data/data_1_1.csv", "r") as myfile: 
    for line in myfile:
        numbers.append(int(line))

# declare variables to store the returned numbers
num1 = 0
num2 = 0

# loop through the numbers list to see which pair adds up to 2020
# then store this pair of numbers in the return variable
for i in numbers:
    for j in numbers:
        if i + j == 2020:
            num1 = i
            num2 = j

# print the results
print("First number: ", num1)            
print("Second number: ", num2)
print("Product: ", num1*num2)
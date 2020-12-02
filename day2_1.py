# day 2 problem 1
# declare an empty lsit to store the numbers
lines = []
# read the file into the list
with open("data/data_2_1.csv", "r") as myfile: 
    for line in myfile:
        lines.append(line)
        
# declare the emplty list required to store teh various data
limits = []
limits_as_ints = []
min_allowed = []
max_allowed = []
letter_to_check = []
passwords = []

#loop through the lines and split them into limits, letter to check and password
for line in lines:
    split_line = line.split()
    limits.append(split_line[0].split('-'))
    letter_to_check.append(split_line[1][0])
    passwords.append(split_line[2])

#loop through limits and break it out into max and min (convert to int) 
for i in limits:
    min_allowed.append(int(i[0]))
    max_allowed.append(int(i[1]))

# for loop the lenght of the lists - check to see how many times the required letter shows up in each password and store in a new list 
letter_count = []
for i in range(len(passwords)):
    letter_counter = 0
    for letter in passwords[i]:
        if letter == letter_to_check[i]:
            letter_counter = letter_counter + 1
    letter_count.append(letter_counter)        

           
# loop through the lenght of the lists check that the number of letter in the password fit the criteria and sum the number that do
allowable_passwords = 0
for i in range(len(passwords)):
    if (letter_count[i]>= min_allowed[i]) and (letter_count[i]<= max_allowed[i]):
        allowable_passwords = allowable_passwords + 1

# print the result
print(allowable_passwords)        
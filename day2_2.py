# day 2 problem 2
# declare an empty lsit to store the numbers
lines = []
# read the file into the list
with open("data/data_2_1.csv", "r") as myfile: 
    for line in myfile:
        lines.append(line)
        
# declare the emplty list required to store the various data
limits = []
limits_as_ints = []
first_position = []
second_position = []
first_letter = []
second_letter = []
letter_to_check = []
passwords = []

#loop through the lines and split them into limits, letter to check and password
for line in lines:
    split_line = line.split()
    limits.append(split_line[0].split('-'))
    letter_to_check.append(split_line[1][0])
    passwords.append(split_line[2])

#loop through limits and break it out into first postion and second postion
for i in limits:
    first_position.append(int(i[0])-1)
    second_position.append(int(i[1])-1)

#loop through the passwords and store the relevant letters as first_letter and second_letter
for i in range(len(passwords)):
    first_letter.append(passwords[i][first_position[i]])
    second_letter.append(passwords[i][second_position[i]])
 
           
# loop through the lenght of the lists check that the number of letter in the password fit the criteria and sum the number that do
allowable_passwords = 0
for i in range(len(passwords)):
    if (first_letter[i] == letter_to_check[i]) and (second_letter[i] != letter_to_check[i]) or (first_letter[i] != letter_to_check[i]) and (second_letter[i] == letter_to_check[i]):
        allowable_passwords = allowable_passwords + 1

# print the result
print(allowable_passwords)        
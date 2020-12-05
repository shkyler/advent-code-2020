# day 4 problem 1

# declare an empty lsit to store the patterns
current_dict = {}
passports = []
# read the file into the list

with open("data/data_4_1.csv", "r") as myfile:
    for line in myfile:
        # if the line is blank, and the dictionary is not empty, add the dictionary to the passport list and clear the dictionary
        if line == '\n':  
            if bool(current_dict):
                passports.append(current_dict)
                current_dict = {}
        # if there is data on the line, remove the line ending, split based on spaces, then split these based on the colon and add them to the current dict as a kv pair
        else:
            line.strip('\n')
            values = line.rsplit()
            for value in values:
                pairs = value.split(':')
                current_dict.update({str(pairs[0]):str(pairs[1])})

#these are the required keys to check       
required_keys = ['hcl', 'pid', 'byr', 'eyr', 'iyr', 'ecl','hgt']
# counbt the valid passports
count = 0
for passport in passports:
    # count the amount of keps preesent in each passport
    key_count = 0
    for required_key in required_keys:
        if required_key in passport:
            key_count = key_count + 1
        # if all 7 are present add it to the total count    
        if key_count == len(required_keys):
            count = count + 1      


print(count)        

# day 3 problem 1 & 2

# declare an empty lsit to store the patterns
lines = []
# read the file into the list
with open("data/data_3_1.csv", "r") as myfile: 
    for line in myfile:
        #use rstrip to remoe the line endings from the patterns
        lines.append(line.rstrip())

# calculate how many times the pattern needs to repeat for the given inputs
times_to_repeat = 200

# note that i created bigger patterns and compared them - I'm sure is mathemaically possbile to solve this probelm without resorting to this
# store the bigger patterns in a bigger list
expand_lines = []
for line in lines:
    ret_val = line
    for i in range(times_to_repeat):
        ret_val = ret_val + line
    expand_lines.append(ret_val)

# declare the required variables for the problem

product = 1 

test_inputs = [[1,1],[3,1],[5,1],[7,1],[1,2]]
results = []

# for each pair of test inputs (x/y coordinates as defined by the problem)
for i in test_inputs:
    #define some ideces for the loops
    row_index = 0
    index = 0
    no_of_trees = 0
    # loop through the list of patterns
    while row_index < len(expand_lines):
        # if a tree is at the coordinate, count it
        if expand_lines[row_index][index] == '#':
            no_of_trees = no_of_trees + 1
        # increase the indices by the values define by the test pair    
        index = index + i[0]
        row_index = row_index + i[1]     
    # store the result in a list    
    results.append(product * no_of_trees) 
  
# loop through the results and return the product  
final_result = 1
for result in results:
    final_result = final_result * result

print(final_result)    

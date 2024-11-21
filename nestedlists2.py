
"""how to print all of the multiples of two from a list of 50 to 123, by slicing a list"""
list_150 = [i for i in range (1,150)]  #create an original list
listoftwo = list_150[51:123:2]  #create list specifying what you want to count

print (listoftwo) #print the list

"""how to achieve the same by using a while loop"""
# Create the original list of numbers from 1 to 149
list_150 = [i for i in range(1, 150)]

# Define the starting index and the ending index
start = 50  # This is the index where the number 50 starts
end = 123   # We want to go up to the index where 123 is included

# Initialize a while loop to go through the range from start to end
i = start
multiples_of_two = []

# Loop through the list and check for multiples of 2
while i <= end:
    if i % 2 == 0:  # Check if the number is even (multiple of 2)
        multiples_of_two.append(i)
    i += 1  # Increment the index to move to the next number

# Print the result
print(multiples_of_two)


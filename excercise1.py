# Ask the user to input a number

num = int(input("Enter a number: "))

# Initialize a variable to hold the sum
total_sum = 0

# Loop through numbers from 1 to the entered number (inclusive)
for i in range(1, num + 1):
    total_sum += i  # Add the current number to the total sum

# Print the result
print(f"The sum of all numbers from 1 to {num} is: {total_sum}")

"""User Input: The program first asks the user to enter a number using the input() function. The input is converted to an integer using int().
Sum Calculation: The program initializes a variable total_sum to store the sum. Then, it uses a for loop to iterate over all numbers from 1 to the entered number (inclusive). In each iteration, the number i is added to total_sum.
Output: After the loop finishes, it prints the calculated sum."""


"""same task with the addition of a function"""

def num():
    # Ask for user input inside the function and return the value
    return int(input("Enter a number: "))

# Get the number from the function
number = num()

# Initialize a variable to hold the sum
total_sum = 0

# Loop through numbers from 1 to the entered number (inclusive)
for i in range(1, number + 1):
    total_sum += i  # Add the current number to the total sum

# Print the result
print(f"The sum of all numbers from 1 to {number} is: {total_sum}")


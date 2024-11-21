"""import random

# Create a random list of length 500 containing integers between 125 and 2250
random_list = [random.randint(125, 2250) for _ in range(500)]

# Print the list (optional, can be large so printing the first 10 values for clarity)
print(random_list[:10])  # Printing the first 10 elements to check

# Find numbers divisible by 5 using list comprehension
divisible_by_5 = [num for num in random_list if num % 5 == 0]

# Print the list of numbers divisible by 5
print(divisible_by_5)"""

import random
def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return
        return True

prime_numbers = []
odd_numbers []
even_numbers []

random_list = [random.randint(125, 2550) for _ in range(500) ]

for number in random_list:
    if check_prime(number):
        prime_numbers.append(number)
    elif
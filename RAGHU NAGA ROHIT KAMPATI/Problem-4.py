# Take input from the user
user_input = input("Enter numbers separated by commas: ")

# Convert input string into a list of integers
nums = [int(x.strip()) for x in user_input.split(",")]

# Dictionary to store results
result = {}

# Loop through numbers 1 to 9
for i in range(1, 10):
    count = 0
    for n in nums:
        if n % i == 0:
            count += 1
    result[i] = count

print(result)

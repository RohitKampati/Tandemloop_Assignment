a = int(input("Enter a: "))

# If 'a' is even, reduce by 1 to get odd count
if a % 2 == 0:
    n = a - 1
else:
    n = a

# Print n odd numbers
print("Output:", end=" ")
for i in range(1, 2*n, 2):
    print(i, end=" ")
print("Enter value of x:")
x = int(input())
print("Enter value of y:")
y = int(input())
x = x ^ y # applying xor to x and y and assigning to x
y = x ^ y # applying xor to x and y and assigning to y
x = x ^ y # applying xor to x and y and assigning to x
print("Value of x:", x)
print("Value of y:", y)

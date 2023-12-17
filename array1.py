"""A program which takes two digits and generates a two dimensional array"""
X, Y = map(int, input("Enter two digits (X, Y): ").split(','))

# Initialize a 2D array filled with zeros
array = [[0 for j in range(Y)] for i in range(X)]
for i in range(X):
    for j in range(Y):
        array[i][j] = i * j
for row in array:
    print(row)

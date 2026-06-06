# Task 2: Matrix Operations
# Part B: Diagonal Sums
# Author: Chiklit Gohil
# Date: 2026-06-06

# take in the matris size
matrixSize = int(input("Size of square matrix: "));

# init the matrix
matrix = []

# take then matrix as input
print("Input the matrix: ")
for i in range(matrixSize):
  matrix.append(input().split(" "));

# convert the string elements to ints
for i in range(matrixSize):
  for j in range(matrixSize):
    matrix[i][j] = int(matrix[i][j]);

# the logic to get the sum of the primary and secondary diagonals
primaryDiagonalSum = 0;
secondaryDiagonalSum = 0;
for i in range(matrixSize):
    primaryDiagonalSum+= matrix[i][i];
    secondaryDiagonalSum+= matrix[i][matrixSize-1 - i];

# print the solutions to the problems in the specified manner
print(f"Primary Diagonal Sum = {primaryDiagonalSum}");
print(f"Secondary Diagonal Sum = {secondaryDiagonalSum}");
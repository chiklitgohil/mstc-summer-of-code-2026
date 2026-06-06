# Task 2: Matrix Operations
# Part A: Matrix Transpose
# Author: Chiklit Gohil
# Date: 2026-06-06

# Take in the rows and column for the matrix you wnat to transpose as input
rows = int(input("Enter the number of rows: "));
col = int(input("Enther the number of col: "));

# initialise out array
a = [];

# run a for loop for me to take the rows as input and appedn the row in into individual col elements using ths split
for i in range(rows):
    a.append(input().split(' '));

# turn the arr elements into INTs rather than the strings
for i in range(rows):
    for j in range(col):
        a[i][j] = int(a[i][j]);

# print the array as a transposed array as requred by the problem statement
for i in range(col):
    for j in range(rows):
        print(a[j][i],end=" ");
    print("\n", end="");
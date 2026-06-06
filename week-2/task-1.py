# Task 1: find the unique elements of the array
# Author: Chiklit Gohil
# Date: 2026-06-06

s = input(); # takes this string as input from user

s = s.strip('['); # remove the right bracket
s = s.strip(']'); # removes the left bracket
arr = s.split(', '); # splits the string using dilimiter and stores it in a list;

set = set(); # creat new which will only store out unique values
for i in range(len(arr)): # a for loop to iterate throug the arr and insert int into the set converting to string to int
  set.add(int(arr[i]));

arr = list(set); # conver the set back to list using this list() function since the output required it to be this way.
print(arr); # print the result.
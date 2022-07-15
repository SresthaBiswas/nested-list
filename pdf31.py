# Given the start and end of a range, write a Python program to print all negative 
# numbers in a given range.
# Example:
# Input: start = -4, end = 5
# Output: -4, -3, -2, -1
a=int(input("enter start of range"))
b=int(input("enter end range"))
for i in range(a,b):
    if i<0:
        print(i,end=',')
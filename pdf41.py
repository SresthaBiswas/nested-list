# Write a Python program to find the dimension of a given matrix.
# Original list:
# [[1, 2], [2, 4]]
# Dimension of the said matrix:
# (2, 2)
# Original list:
# [[0, 1, 2], [2, 4, 5]]
# Dimension of the said matrix:
# (2, 3)
# Original list:
# [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
# Dimension of the said matrix:
# (3, 3)
list=[[0, 1, 2], [2, 4, 5]]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        j=j+1
    i=i+1
print(i,j)
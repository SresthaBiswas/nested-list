# Write a Python program to pair up the consecutive elements of a given list.
# Original lists:
# [1, 2, 3, 4, 5, 6]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
list=[1, 2, 3, 4, 5, 6]
i=0
l=[]
while i<len(list)-1 :
    l1=[]
    a=list[i]
    l1.append(list[i])
    l1.append(list[i+1])
    i=i+1
    l.append(l1)
print(l)    
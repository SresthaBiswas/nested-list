# Write a Python program to convert a given list of strings into list of lists.
# Original list of strings:
# ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]
list=["red","maroon","yellow","olive"]
i=0
l=[]
while i<len(list):
    l1=[]
    j=0
    while j<len(list[i]):
        l1.append(list[i][j])
        j=j+1
    l.append(l1)
    i=i+1
print(l)
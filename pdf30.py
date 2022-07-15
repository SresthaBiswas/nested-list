# Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
# Iist2 = [-12, 14, 95, 3]
# Output: pos = 3, neg = 1
list=[2, -7, 5, -64, -14]
i=0
neg=0
pos=0
while i<len(list):
    if list[i]<0:
        # print("neg =",list[i])
        neg=neg+1
    elif list[i]>0:
        # print("pos =",list[i])
        pos=pos+1
    else:
        pass
    i+=1   
print("pos =",pos,",","neg =",neg,)    
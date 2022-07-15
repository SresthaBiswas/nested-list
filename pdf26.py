# Our task is to print the element which occurs 3 consecutive times in a Python list.
# Example:
# Input: [4, 5, 5, 5, 3, 8]
# Output: 5
# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output: 1, 22
list=[4, 5, 5, 5, 3, 8]
i=0
l=[]
while i<len(list)-1:
    if list[i]==list[i+1] and list[i+1]==list[i+2]:
        print(list[i])
    else:
        pass    
    i=i+1    
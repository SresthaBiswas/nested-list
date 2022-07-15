# Write a Python program to join adjacent members of a given list.
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']
# Original list:
# ['1', '2', '3']
# Join adjacent members of a given list:
# ['12']
list=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
j=1
l=[]
while i<len(list) and j<len(list):
    a=list[i]+list[j]
    l.append(a)
    i+=2
    j+=2
print(l)    
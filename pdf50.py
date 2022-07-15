# Write a Python program to join two given list of lists of same length, element wise.
# Original lists:
# [[10, 20], [30, 40,45,34], [50, 60], [30, 20, 80]]
# [[61,42], [12, 14, 15], [12, 13, 19, 20], [12]]
# Join the said two lists element wise:
# [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
# Original lists:
# [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
# Join the said two lists element wise:
# [['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]
list1=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
list2=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
l=[]
while i<len(list1):
    a=list1[i]+list2[i]
    l.append(a)
    i=i+1
print(l)
# try other way
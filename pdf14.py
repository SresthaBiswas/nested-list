# Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# # (1, [0])
list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
max=0
min=len(list[i])
c=0
while i<len(list):
    a=len(list[i])
    if a>max:
        max=a
        b=list[i]
    elif a<min:
        min=a
        c=list[i]
        print(c)
    i+=1
print("(",max,",",b,")") 
print(min,c) 
abh
c not defining
# list=[1,2,3,4,5,6]
# i=0
# max=0
# min=list[i]
# while i<len(list):
#     if list[i]>max:
#         max=list[i]
#     if list[i]<min:
#         min=list[i]
#     i+=1
# print(max,min)
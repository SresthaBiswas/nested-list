# Write a Python program to check if first digit/character of each element in a given list
# is same or not.
# Original list:
# [1234, 122, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not!
# True
# Original list:
# [1234, 922, 1984, 19372, 100]
# Check if the first digit in each element of the given list is the same or not!
# False
# Original list:
# ['aabc', 'abc', 'ab', 'a']
# Check if first character in each element of the said given list is same or not!
# True
# Original list:
# ['aabc', 'abc', 'ab', 'ha']
# Check if first character in each element of the said given list is same or not!
# False
# list=[1234, 122, 1984, 19372, 100]
# i=0
# c=str(list[0])
# a=c[0]
# while i<len(list):
#     b=str(list[i])
#     d=b[0]
#     if a==b:
#         print("true")
#     else:
#         pass
# i=i+1    
list=["1234", "122", "1984", "19372", "100"]
i=0
while i<len(list):
    if str(list[i][0])==str(list[i+1][0]):
        print("true")
    else:
        print("false")    
    i=i+1
    index out of range
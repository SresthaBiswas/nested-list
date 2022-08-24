# Write a Python program to iterate a given list cyclically on specific index position.
# Original list:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Iterate the said list cyclically on specific index position 3 :
# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
# Iterate the said list cyclically on specific index position 5 :
# ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']
list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a=3 
# (int(input("enter index position"))
i=0
l=[]
while i<len(list):
    a=list[i]
    j=0
    while j<list[a]:
        b=list[j]
        l.append(b)
    # list.remove(list[i])
    # list.append(list[i])
    # list.remove(list[i])
    # if i==a:
    #     break
    i+=1
    j=j+1
print(l)
incomplete
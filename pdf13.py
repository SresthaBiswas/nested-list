# [[2, 1], 2, 3, [2, 4], 5, 1]
# list=[1, 1, 2, 3, 4, 4, 5, 1]
# newlist=[]
# i=0
# count=0
# while i<len(list):
#     a=list[i]
#     if i==i+1:
#         print
list1 = [1,1,2,3,4,4,5,1]
list2 = list()
l1 = [ ]
i = 0
while i < len(list1):
    if list1[i] not in list2:
        list2. append(list1[i])
    i += 1
j = 0 
while j < len(list2):
    list3 = list()
    a = list1.count(list2[j])
    list3.append(a)
    list3.append(list2[j])
    l1.append(list3)
    j += 1
print (l1)
# Write a Python program to compute the average of n th elements in a given list of
# lists with different lengths.
# Original list:
# [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average of n-th elements in the said list of lists with different lengths:
# [4.8, 5.8, 6.8, 8.0, 11.0]
list=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
i=0
# sum=0
count=0
# avg=0
l=[]
while i<len(list):
    # a=list[i]
    j=0
    sum=0
    avg=0
    while j<len(list[i]):
        # count=count+1
        sum=sum+list[i][j]
        avg=sum//len(list[i])
        l.append(avg)
    j=j+1
i=i+i
print(l)        
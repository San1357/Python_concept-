# Problem:
'''You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
'''



#CODE:


list1 = []
n = int(input("enter the amount of number you want to put in list:"))
newList = []

for i in range(0,n):
    ele = int(input())
    list1.append(ele)
    newList.append(ele*ele)
print(list1)
print(newList)

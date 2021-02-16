#Problem:How to take user input to make a list.




#CODE:

lst = []
n = int(input("enter no. of elements:"))

for i in range(0,n):
    ele = int(input("enter the number line by line:"))
    lst.append(ele)
    
print(lst)

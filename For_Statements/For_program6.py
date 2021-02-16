'''#Problem:Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, 
if found. Iterate over list using for loop
'''


#CODE:


lst = []
n = int(input("enter no. of elements:"))

for i in range(0,n):
    ele = int(input("enter the number line by line:"))
    lst.append(ele)
    
print(lst)

a = int(input("again enter any no. that you want to delete from  the list:"))
if a in lst:
    lst.remove(a)
    print("After deleting the elements from list:",lst )
else:
    print("Sorrry!!! We didn't find your number in the list:",lst)
    

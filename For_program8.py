'''PROBLEM: 
Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers. '''





#CODE: 

list1 = [] # this list is store even number.
#n = int(input("enter the amount of number you want to put in list:"))
List2 = [] # this list is store odd number.

for i in range(1,101):
    if i%2==0:
        list1.append(i)
        
    else:
        List2.append(i) 
        
print(list1)
print(List2)
    
    
    
#OUTPUT:

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]



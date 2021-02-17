#Problem :
'''From the two list obtained in previous question, make new lists,
containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
'''

#CODE :

list1 = [] # this list is store even number.
#n = int(input("enter the amount of number you want to put in list:"))
List2 = [] # this list is store odd number.
listdivisibleby4 = [] # this list store the number divisible by 4
listdivisibleby6 = [] # this list store the number divisible by 6
listdivisibleby8 = [] # this list store the number divisible by 8
listdivisibleby10 = [] # this list store the number divisible by 10
listdivisibleby3= [] # this list store the number divisible by 3
listdivisibleby5 = [] # this list store the number divisible by 5
listdivisibleby7 = [] # this list store the number divisible by 7
listdivisibleby9 = [] # this list store the number divisible by 9

for i in range(1,101):
    if i % 2 == 0:
        list1.append(i)
    if i % 4 == 0:
        listdivisibleby4.append(i)
    if i % 6 == 0:
        listdivisibleby6.append(i)
    if i % 8 == 0:
        listdivisibleby8.append(i)    
    if i % 10 == 0:
        listdivisibleby10.append(i)
    if i % 3 == 0:
        listdivisibleby3.append(i)
    if i % 5 == 0:
        listdivisibleby5.append(i)
    if i % 7 == 0:
        listdivisibleby7.append(i)
    if i % 9 == 0:
        listdivisibleby9.append(i)    
    if i % 2 != 0:
        List2.append(i) 
        
print(list1)
print(List2)

print(listdivisibleby4)
print(listdivisibleby6)
print(listdivisibleby8)
print(listdivisibleby10)
print(listdivisibleby3)
print(listdivisibleby5)
print(listdivisibleby7)
print(listdivisibleby9)

#OUTPUT:

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100]
[6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
[8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
[9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]







    

    

''' Problem : Write a python program to read three numbers (a,b,c) and check how many numbers between ‘a’ and ‘b’ are divisible by ‘c


#CODE:

a = int(input("enter any number:"))
b = int(input("enter any number:")) 
c = int(input("enter any number:"))
lst=[]
for i in range(a,b):
    if i % c == 0:
        lst.append(i)
        print("these number are divisible by c:", i)
        
print(lst)
print(len(lst))


#OUTPUT:

enter any number:2
enter any number:20
enter any number:2
these number are divisible by c: 2
these number are divisible by c: 4
these number are divisible by c: 6
these number are divisible by c: 8
these number are divisible by c: 10
these number are divisible by c: 12
these number are divisible by c: 14
these number are divisible by c: 16
these number are divisible by c: 18
[2, 4, 6, 8, 10, 12, 14, 16, 18]
9



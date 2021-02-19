'''
Problem: Write a python program to print the factorial of a given number'''


#CODE:

n = int(input("enter any number:"))
factorial = 1 

if n < 0:
    print("factorial does not exist of negative number.!! Thank You !!!")
else:
    
    for i in range(1,n+1):
        factorial = factorial* i 
    print(factorial)

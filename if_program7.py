#Problem:

'''
Write a program to print absolute vlaue of a number entered by user. E.g.-
INPUT: 1        OUTPUT: 1
INPUT: -1        OUTPUT: 1 
'''


#Code:

user_no = int(input("enter any number:"))
if user_no == 0:
    print ("0")
elif user_no < 0:
    print(abs(user_no))
else :
    print(user_no)

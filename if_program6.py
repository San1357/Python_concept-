# Problem :

'''Take input of age of 3 people by user and determine oldest and youngest among them.'''



age1 = int(input("enter your age :"))
age2 = int(input("enter your age :"))
age3 = int(input("enter your age :"))

if (age1 < age2) and (age1 < age3):
    print("person1 is yonger from both of them")
    if (age2 <age3):
        print("person3 is older from both of them.")
    else:
        print("person2 is older from both of them.")
        
elif (age2 < age1) and (age2 < age3):
    print("person2 is yonger from both of them")
    if (age1 <age3):
        print("person3 is older from both of them.")
    else:
        print("person1 is older from both of them.")

elif (age3 < age2) and (age3 < age1):
    print("person3 is yonger from both of them")
    if (age2 <age1):
        print("person1 is older from both of them.")
    else:
        print("person2 is older from both of them.")
        




    

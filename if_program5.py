# Problem:
'''A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.'''




marks = float(input("enter your marks:"))
if marks < 25 :
    print ("Your Grade is:F")
elif (marks >= 25) and (marks <45):
    print ("Your Grade is:E")
elif (marks >= 45) and (marks <50):
    print ("Your Grade is:D")
elif (marks >= 50) and (marks <60):
    print ("Your Grade is:C")
elif (marks >= 60) and (marks <80):
    print ("Your Grade is:B")
elif (marks >= 80) and (marks <=100):
    print ("Your Grade is:A")
else:
    print("This is not possible because paper is of 100 only. Re-enter your marks.")

    

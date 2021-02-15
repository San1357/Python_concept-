#Problem:

'''

A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''

#Code:


Total_no_class_held = int(input("enter the no. of class held:"))
no_of_class_student_attended = int(input("enter the no. of class the student attended:"))
percetageOfClassAttended = (no_of_class_student_attended * 100)/Total_no_class_held

if percetageOfClassAttended < 75 :
    print("Sorry, You aren't eligible to sit in exam cause your attendance is very low.")
else :
    print("Congratulations!!! You are eligible for the exam. BEST Of LUCK. ")

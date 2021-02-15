#Problem:

'''A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.'''

#CODE:
year_of_service = float(input("Enter the year of service:"))
#current_salary = float(input("Enter the current salary:"))
#fivePercentOfYourSalary = ((5 * current_salary)/100)
#YourSalaryafter5percentbonus = current_salary + fivePercentOfYourSalary

if year_of_service <= 5 :
    print("Sorry, This Scheme is not for You.So better focus on your job now .")

else:
    current_salary = float(input("Enter the current salary:"))
    fivePercentOfYourSalary = ((5 * current_salary)/100)
    YourSalaryafter5percentbonus = current_salary + fivePercentOfYourSalary
    print("Congratulations!!! Here is your salary after 5% bonus:", YourSalaryafter5percentbonus)

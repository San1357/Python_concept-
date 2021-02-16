# NOTE: Given below code is not working.


#CODE:
import calendar 
import pytz
from datetime import datetime, timedelta 
import datetime 


date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
def findDay(date1): 
    
   # day, month, year = (int(i) for i in date.split(' '))     
    dayNumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"] 
    return (days[dayNumber]) 
    
  
#date = str(input("enter the date:"))
a=findDay(date1)
print(a)


lstOfDays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]


if a in lstOfDays:
    tz_INDIA = pytz.timezone('Asia/Kolkata') 
    datetime_INDIA = datetime.now(tz_INDIA)
    IST_time = datetime_INDIA.strftime("%H:%M:%S")
    if IST_time >= '11:00:00' and IST_time <= '18:15:00' :
        print("He's is Coding")
    elif IST_time >='19:30:00' and IST_time <= '22:00:00':
        print("either He's doing sketching or playing valorant.")
    elif IST_time >= '22:30:00' :
        print("shhhh..sshhhh..!!! He's sleeping. Dont disturb him.")
else: 
    print("Timepass :)(:")



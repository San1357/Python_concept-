#Problem:
'''A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
'''

quantity = int(input("enter the quantity number:"))
unit = 100
discount_price_range = 1000
priceOfyour = quantity * unit
TenpercentofyourPrice = ((10 * priceOfyour)/100) 
afterdiscountPrice = priceOfyour - TenpercentofyourPrice
if priceOfyour <= 1000:
    print("Sorry. There is no discout you will get.")
else:
    print("Congratulation!!! Here is your after discount Price:", afterdiscountPrice)

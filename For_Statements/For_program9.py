'''Problem:
Python Program to Calculate Sum of Even Numbers from 1 to 10'''

#CODE:

_sum=0
for i in range(0,11):
    if i % 2 ==0:
        _sum = _sum+i
print(_sum)


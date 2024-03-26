# Day of the Week
# Output message depending on the day of the week
# Author: Janelle Cunningham

import datetime

today = datetime.datetime.today()
print(today)

if today.weekday() <5:
    print("Yes, unfortunately today is a weekday.")   

elif today.weekday() == 5 or today.weekday() == 6:
    print("It is the weekend, yay!")

                       
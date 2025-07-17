#write to python code to get a current datatime

import datetime

today = datetime.datetime.now()
formatted = today.strftime("%d-%m-%Y %I:%M:%S %p")#%I--1 TO 12 HOURS FORMAT, %P--AM/PM,%H--0 TO 24 HRS
print("Current Date and Time:", formatted)


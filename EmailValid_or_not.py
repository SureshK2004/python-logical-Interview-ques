#write a python program to check the email is valid or not

import re

def isvalid(email):
    regex="^[A-Z0-9.%+-]+@[A-Z0-9]+\.[A-Z]{2,}$"
    if len(email) > 7:
        return True
    
if isvalid("suresh@org.in"):
    print("its a valid email address")
else:
    print("its not email address")

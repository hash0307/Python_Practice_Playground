"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).
"""

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # print(type(s))
    t = list(s.split(":"))
    # print (t)
    if "PM" == s[-2:] and int(t[0]) < 12:
        # t = list(s.split(":"))
        t[0]= str(12 + int(t[0]))
        t = ":".join(t)
        # t[-1].replace("PM","")
        # t[-1].removesuffix("PM")
        return t[:-2]
    elif "AM" == s[-2:] and s[:2] == "12":
        t[0] = "00"
        t = ":".join(t)
        return t[:-2]
    # return t
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()

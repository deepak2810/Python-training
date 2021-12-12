# Python program to print random element along with empty spaces from a list using random package

import random

team = ["deepak","manish","asish","rahul","amit","mayank","vikash","ajay","sanjay","raju","ajeet"]

l = len(team)
k= random.randint(0,l-1)
print(team[k])
s=""
for i in team[k]:
    s+="_ "
print(s)    
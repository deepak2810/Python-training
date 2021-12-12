# python program to print random elements from string using random package.

import random

Tut = [ "aarav","meethi","priyanshu","mohit"]

k = len(Tut)
s=""
for i in range(k):
    l=random.randint(1,k-1)
    s+=" _ "
    print(Tut[l])
    print(s)
# a python program to find the sum of the list element

def sumOflist(ls):
    sumof = 0
    for i in ls:
        sumof+=i

    return sumof

ls = [10,20,30,50]

print(sumOflist(ls))
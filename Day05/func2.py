# python program to find minimum number from the list using user defined function
def mino(ls):
    mini = 10000000000

    for i in ls:
        if i<mini:
            mini=i

    return mini

# ls=[12,20,45,65,77,80]
# # calling the function
# print(mino(ls)) 

ls1=[10,-2,345,889]
print(mino(ls1))





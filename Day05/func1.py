def length(ls):
    count =0;

    for i in ls:
        count+=1

    return count

# ls=[1,3,45,54,68] 
# print(length(ls))   

ls=[100,200,400,600]
print(length(ls))
for i in range(length(ls)):
    print(ls[i])
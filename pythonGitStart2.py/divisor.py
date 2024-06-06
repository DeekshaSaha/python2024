num=int(input("please choose a number to divide : "))
list1 = list(range(1,num+1))
divlist=[]
for num1 in list1 :
    if num%num1==0:
        divlist.append(num1)
print(divlist)
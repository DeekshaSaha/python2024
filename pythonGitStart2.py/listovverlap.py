list1=[2,5,6,8,10,26]
list2=[2,5,8,8,10,28]
commonlist=[]
for a in list1:
    if a in list2:
        if a in commonlist:
            continue
        else:
            commonlist.append(a)
print(commonlist)
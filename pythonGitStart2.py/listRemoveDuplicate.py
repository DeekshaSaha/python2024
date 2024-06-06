a=[1,1,1,2,2,3,4,5,8,8,9,9,10]
for number in a:
    for i in a:
        if number==i:
            a.remove(number)
print(a)
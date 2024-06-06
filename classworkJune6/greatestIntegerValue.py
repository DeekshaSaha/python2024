n = input("enter a number ")
nlist=list(n)
newlist = []
for i in range(0,len(nlist)-1):
    if nlist[i] == ".":
        break
    newlist.append(nlist[i])
b = ''.join(map(str,newlist))
c=int(b)
print(c)


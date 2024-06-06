''' print the first n fibonacci number , and find the 
mean golden ratio of them, 
take n from user , 
WARNING PLEASE DO NOT ENTER VALUE MORE THAN 100000'''
n=int(input("how many do you want to print : "))
F=[]
F.append(1) # esme 1 agaya he list me 
F.append(1) # esme bhi a gaya he
g=3 
count = 0
i=1 # pehele ke sath usse minus karke next value ke liye jisse hamne bad me bara diya he jisse loop me vo no.lete rahe 
while count < n-2: # yaha -2 kiya he kyuki bina minus 2 ke yaha 2 zada no a jayega 
    x= F[i]+F[i-1]
    F.append(x)
    g = g+(F[i]/F[i-1]) # golden ratio sirf f se he 
    count+=1
    i+=1
#print(F)
print(g/n)

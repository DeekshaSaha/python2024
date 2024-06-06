'''
print the first the n prime number , n is given by user 
'''
n=int(input("how many prime no. you want to print: "))
list1 = []
x = 2
count = 0
def isPrime(a):
    flag=0
    for i in range(2,a):
        if a%i==0:
            flag=1
            break
    if flag==0:
        return a 
    elif flag==1:
        return 0
while count < n :
    y = isPrime(x)
    if y != 0:
        list1.append(y)
        count+=1 
    x+=1
print(list1)


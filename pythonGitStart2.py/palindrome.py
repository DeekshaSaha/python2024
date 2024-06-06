# palindrome number 
'''num=int(input("enter a number :"))
n = 0 
while num>0 :
    n= n*10 + (num%10)
    num=num//10
if num==n :
    print("is a palindrome no.")
else:
    print("is not a palindrome no.")'''
num=input("enter a word or number :")
list1=list(num)#yaha hamne list me liya he num ko
l=len(list1)# isme len se gin liya he 
if l%2==0: # check kar rahe he even or odd ka or ha n lo he yaha vo bata ta he ki kitne bar loop chalega 
    n=l/2 # even 
else :
    n=(l-1)/2 # odd but L-1 HE YAHA kyu ki hame odd se even me lane ke liye 
x=0
flag=0
while x<n :
    if list1[x]==list1[l-1]: # yaha check kar rahe he ki vo he ya nahi 
        x+=1
        l-=1
        flag=0 # ye bata raha he ki agar he toh flag =0 he 
    else :
        flag=1 # nahi he toh yaha a jayega 
        break
if flag==0:
    print ("paindrome true")
else:
    print ("palindrom false")
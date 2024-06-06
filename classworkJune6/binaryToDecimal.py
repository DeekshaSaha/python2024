import math
ans = input("Choose following conversion method: \n\t(1) Binary to Decimal \n\t(2) Decimal to Binary\n\n\t")
if ans == "1":
    num = input("enter a binary number : ")
    numlist = list(num)
    numlist.reverse()
    n = 0
    a = 0
    for i in numlist:
        a = a + int(i)*2**n
        n+=1
    print(a)
elif ans == "2":
    num3 = int(input("enter a int number : "))
    binlist = []
    while num3 != 0 :
        binlist.append(num3%2) 
        num3 = math.floor(num3/2)
    binlist.reverse()
    b = ''.join(map(str,binlist))
    print(b)
else:
    print("invalid option")





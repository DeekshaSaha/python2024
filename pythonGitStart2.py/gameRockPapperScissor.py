i1 = input("enter your choice: ")

i2 = input("enter your choice: ")

if i1 == i2:
    print("tie")
elif i1=="rock":
    if i2=="scissor":
        print("rock wins")
    else:
        print("paper wins")
elif i1=="scissor":
    if i2=="paper":
        print("scissor wins")
    else:
        print("rock wins")
elif i1=="paper":
     if i2=="rock":
         print("paper wins")
    else:
         print("scissor wins")
else:
print("invalid input")
import sys
sys.exit()


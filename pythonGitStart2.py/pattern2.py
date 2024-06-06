'''for i in range(0,5):
    for j in range(0,i+1):
        print("*", end="")
    print()'''
z=5
for i in range (0,z):
    for j in range (0,z-i):
        print(" ", end=" ")
    for j in range (0,i+1):
        print ("*",end=" ")
    print()  
z=5
for i in range (z,0,-1):
    for j in range (1,z+1-i):
        print(" ", end=" ")
    for j in range (1,i+1):
        print ("*",end=" ")
    
    print()  



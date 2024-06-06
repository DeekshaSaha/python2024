list1=list(range(1,100,5))
def new_list():
    b=[list1][0],list1[len(list1)-1]
    print(b)
new_list()
a="i am a carrot"
def revstr(a):
    str=" "
    b=a.split()
    b.reverse()
    return(str.join(b))
print(revstr(a))

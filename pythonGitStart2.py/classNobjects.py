'''class fruit:#yaha hamne ek class banaya he 
    edibility = "is edible" # ye sab object he 
    origin = "grows on trees"
    
    def go(self):# yaha function bana or self fruit me jo objects he usse bula raha he 
        print("it ",self.origin)# jse yha origin ko bula raha he 
    def eat(self):# ye or ek function 
        print("it ",self.edibility)   # phir se bula raha he  
class food:#dusra class
    flavor= "is sweet" 

    def taste(self):
        print("it ",self.flavor)

mango = fruit()# ab yaha pe fruits me ham mango ko push kar rahe he matlab mango upar class me jkar apna kam karega function jesa  
mango.go()# or yaha go function ko bula rahi he  
mango.eat()
mango = food()
mango.taste() '''
class fruit:
    def __init__(fruits,name,taste,color):#fruits se baki ki pehechan kar rahe he 
        fruits.name = name #yaha name define ho raha he ; kar raha he fruits.name
        fruits.flavor = taste# sab upar jesa same
        fruits.color = color # same 
    def go(fruits):# ye jakar bula rahahe fruits ko jo define kiya he jese nam , rang orha niche jo + he vo , jesa kam kar raha he   
        print(fruits.name+" is a fruit, it tastes "+ fruits.flavor+" and it is "+str(fruits.color)+" in color")
mango=fruit("🥭","sweet","yellow")#hamne yaha jo nam tha rang tha usme kya nam jese mango vo sab diya he or push bhi kiya he upar fruit me jisse coad chale
mango.go()# call kiya ab sab jo arguments diye he a jayega 
litchi=fruit("litchi","sweet",9)
litchi.go()
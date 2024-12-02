class Dog:
    legs = 4
    eyes = 2
    nose  = 1
    ears = 2
    canFly = False
    def bark(self): #every function in class has the paramenter "self"
        print("Wolf Wolf")

sausageDog =  Dog() #sausage dog is the onbject of the dog class and can now access all properties and functions of it 
print(sausageDog.legs)
sausageDog.bark()
husky = Dog()
print(husky.canFly)









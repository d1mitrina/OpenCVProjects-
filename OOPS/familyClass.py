class Family():
    def __init__(self,name,age,relation):
        self.name = name
        self.age = age
        self.relation = relation
    def eating(self):
        print(" Lets have dinner together! ")
daughter = Family("Dimi",16,"daughter")
print(daughter.name,daughter.age)

brother = Family("Blag",8,"son")
print(brother.age)
brother.eating()

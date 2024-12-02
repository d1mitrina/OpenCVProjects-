class Car():
    def __init__(self,colour,company,model):
        self.colour = colour
        self.company = company 
        self.model = model 
    def isMoving(self):
        print("Car is moving")
    def notMoving(self):
        print("Car is not moving")

car1 = Car("Red","Lambo","93843")
print(car1.colour)
car1.isMoving()

#parent - child class
#concpet of inheritance where you can inherit multiple classes from one base class
class SportsCar(Car):
    def __init__ (self,colour,company,model,engine_type,max_speed):
        Car.__init__(self,colour,company, model)
        self.engine_type = engine_type
        self.max_speed = max_speed
    def  showCar(self):
        print (self.colour,self.company,self.model,self.engine_type,self.max_speed)
        
bmwx11 = SportsCar("Black","BMW","X11","33948","260mph")
bmwx11.showCar()

print(type(5.8765678)) #everything is a class in programming 






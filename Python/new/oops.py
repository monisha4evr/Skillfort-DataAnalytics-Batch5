oops=> object Oriented Programming 
    -  reusablity
    -  organized
    -  real world entity

class  => Blueprint 
object => instance of class 
method/property => function inside class
variable/attribute => 

# Syntax: 
class ClassName : 
    pass
    #statement


class Sample:
    name="Sakthi"
    address="Bangalore"

print(Sample.name)
print(Sample.address)
Sample.name="Arifa"
Sample.city="marathahalli"
print(Sample.city)
print(Sample.name)
setattr(Sample,"pincode",560037)
print(Sample.pincode)
print(getattr(Sample,"address"))
delattr(Sample,'city')

print(getattr(Sample,"city")) # AttributeError: type object 'Sample' has no attribute 'city'
print(Sample.city) # AttributeError: type object 'Sample' has no attribute 'city'


class Test:
    def display():
        print("Welcome")

Test.display()

method type:
1. instance method (self)
2. classmethod  ( @classmethod )
3. static method ( @staticmethod )


# instance method
class Test:
    def display(self):
        print("Welcome")

t=Test()
t.display()
t1=Test()
t.display()
t2=Test()
t.display()


class Test:

    def __init__(self,vname,brand):
        self.vname=vname
        self.brand=brand
    def display(self,color):
        print(f"Vechicle Name : {self.vname} Brand : {self.brand}  Color:{color}")

t=Test("car","BMW")
t.display("red")


# 2. classmethod  ( @classmethod) 
class Vegetable:
    veg_1 ="Potato" 
    veg_2 ="Brinjal" 
    veg_3 ="Carrot" 

    @classmethod
    def display(t):
        print(t.veg_1)
        print(t.veg_2)
        print(t.veg_3)

v=Vegetable()
v.display()


# Static method

class Addition:
    @staticmethod
    def add(a,b):
        print(a+b)
a=Addition()
a.add(5,10)

pillars of Oops Concept
-----------------------

inheritance 
polymorphism
Encapsulation
Abstraction


polymorphism:
1. overloading - same name
2. over riding 


1. overloading - same name

class Calculation :
    @staticmethod
    def add(a,b,c=0,d=None):
        print(a,b,c,d)

c=Calculation()
c.add(4,5)
c.add(5,5,5)
c.add(1,2,3,4)






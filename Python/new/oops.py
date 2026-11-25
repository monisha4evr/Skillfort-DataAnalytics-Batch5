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
    def add(a,b,c=0,d=None,*e):
        print(a,b,c,d,e)

c=Calculation()
c.add(4,5)
c.add(5,5,5)
c.add(1,2,3,4)
c.add(1,2,3,4,5,6,8,7)

# 2. overridding

class Animal:
    def make_sound(self):
        print("Animals make Sound")

class Cat(Animal):
    def make_sound(self):
        print("Cats Says Meoww")

c=Cat()
c.make_sound()

class Animal:
    def make_sound(self):
        print("Animals make Sound")

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("Cats Says Meoww")

c=Cat()
c.make_sound()





#inheritance:

1. single inheritance 
2. multiple inheritance 
3. multi-level inheritance
4. hierarchial inheritance 
5. hybrid inheritance



1. single inheritance 
class Parent:
    def parent_display(self):
        print("Parent Class")

p=Parent()
p.parent_display()

class Child(Parent) :
    def child_display(self):
        print("I am Child")

c=Child()
c.child_display()
c.parent_display()

2. multiple inheritance 
--> Multiple Parent 
-- child 

class Father:
    def display(self):
        print("father")

class Mother:
    def display_mother(self):
        print("Mother")

class Child(Father, Mother):
    def display_child(self):
        print("i am child")

c=Child()
c.display()
c.display_mother()
c.display_child()

# hierarchical inheritance

class Animal:
    def make_sound(self):
        print("Animal makes Sounds")

class Dog(Animal):
    def bark(self):
        print("bow bow")

d=Dog()
d.make_sound()
d.bark()

class Cat(Animal):
    def meow(self):
        print("Meaooow")

c=Cat()
c.make_sound()
c.meow()


# multilevel 

class Grandparent:
    def display_g(self):
        print("Grand Parent")

class Parent(Grandparent):
    def parent_display(self):
        print("Parent Class")

class Child(Parent) :
    def child_display(self):
        print("I am Child")

class Gchild(Child):
    def gc_display(self):
        print("grand Child")


g=Gchild()
g.display_g()
g.parent_display()
g.child_display()
g.gc_display()



Encapsulation
- bind data together 

# access specifier 
# public  
#     - anyone can use  
#     eg: Transportation - bus  

# protected - 
#     class and inherited class  
#     eg: scooter, mobile no 
#     => differentiate by adding prefix(_)
# private 
#     - within the class, 
#     eg: OTP,password 
#     => differentiate by adding prefix(__)


to access private method
1. name Mangling  (_classname__variablename)
2. getter/setter

class Userprofile:
    def __init__(self,uname,mbl,pwd):
        self.uname=uname
        self._mbl=mbl
        self.__pwd=pwd 

    def get_password(self):
        print("Password : ", self.__pwd)

    def set_password(self,newpwd):
        self.__pwd=newpwd


u=Userprofile("lega",909090,'123@lega')
print(u.uname)
print(u._mbl)
u.get_password()
u.set_password('lega@123')
u.get_password()
print(u._Userprofile__pwd)
#print(u.__pwd) # AttributeError: 'Userprofile' object has no attribute '__pwd'


abstraction 
- hiding unnecessary  implementation 
- show  important 

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass 
    def display(self):
        print("Simple Example")

class Car(Vehicle):

    def start_engine(self):
        print("Engine Started")
    def display_car(self):
        print("Car started")

c=Car()
c.start_engine()
c.display()
c.display_car()

    
# hybrid 
class Parent:
    def __init__(self):
        print("Parent")

class Father(Parent):
    def __init__(self):
        super().__init__()
        print("Father")

class Mother(Parent):
    def __init__(self):
        super().__init__()
        print("Mother")

class Child(Father , Mother):
    def __init__(self):
            super().__init__()
            print("Child")

c= Child()
print(Child.mro())
print(Child.__mro__)



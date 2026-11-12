# Function:
# ---------

Reusable block of code -> to perform some specific task.

Features:
1. code Reusabilty
2. avoid repitation 
3. code clean and readable 

# Syntax: 
#definition/declaration
def functionname(): 
    #statement
    pass 

# calling 
functionname()


def greet():
    print("Welcome to Function")

greet()

types of function: 

1. built-in-function  eg: (print(),input())
2. user defined 
3. lambda 
4. recursion (function called itself) 

user Defined 
# 1. without argument without return 
# 2. without argument with return 
# 3. with argument without return 
# 4. with argument with return

example for return :
-------------------

def sample():
    print("Welcome to Function Programming")
    return 1
    a=10
    b=20
    print(a+b)
    print("Checking the Return Flow")

print(sample())
res=sample()
print(res)

# return=> break the function and return value

# argument and parameter
# argument => actual value 
# parameter => alias name 


def function_name(parameter): #alias an
    pass 

function_name(argument) # actual value

# note: argument and parament count must be Same

def add(a,b):
    print(a+b) 


add(60,70)
add(45,60)
add(44,89)

x=10
y=50

add(x,y)

# 1. without argument without return 


def add ():
    a=10
    b=20
    print(a+b)
    print(50+90)
    c=int(input("Enter username"))
    d=int(input("enter paswword"))
    if c=="lega" and d=="lega@123":
        print("Success")
    else:
        print("invalid")


add()


# 2. without argument with return 

def add():
    a=10
    b=20
    return (a,b,a+b) 

sakthi,deepal,lega=add() # unpacking
print(sakthi)
print(deepal)
print(lega)

res=add()
print(res)
for i in res:
    print(i)

a,b=20,45
print(a)
print(b)

a,b=[1,2,3]  # ValueError: too many values to unpack (expected 2, got 3)
print(a)
print(b)


# 3. with argument without return 


def add(a,b,c):
    print(a+b+c)

add(20,40,60)

fruit1="apple"
fruit2="orange"
fruit3="banana"
add(fruit1,fruit2,fruit3)


# 4. with argument with return 

def add(a,b):
    return (a+b)

res=add(10,20)
print(res)


Note: argument count must match with parameter count

types of argument 
1. positional argument 
2. keyword argument 
3. arbitary argument
4. default argument


1. positional argument 

def add(x,z):
    print(x)
    print(z)

add(50,30)

2. keyword argument 

def add(x,y,z):
    print(x,y,z)

add(10,x=20,z=30) # TypeError: add() got multiple values for argument 'x'

add(z=10,y=20,x=30)
add(a=10,y=20,x=30)

3. arbitary argument (packing) rest of the element stored in single variable

* => positional -> tuple 
** =>  keyword word  -> dict  

def sample(a,*b):
    print(a,b)

sample(1,2,3,4,5,6,7,8)


def sample(a,**b):
    print(a,b)

sample(a=1,b=2,c=3,d=4,e=5,f=6)

# default 
# positional only 
# keyword only 


# lambda 

# recurrsion

# higher order function (map,reduce,filter)





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

def display(username , login_name="user"):
    print(username)
    print(login_name)

display("sakthi")
display("deepal","Deepal")

def display(count=0):
    print(count)

display()
display(50)

# positional only 


def sample (a,b,c,/):
    print(a,b,c) 

sample(10,20,30)

def sample (a,b,/,c,d):
    print(a,b,c,d) 

sample(10,20,d=40,c=30)
sample(10,20,d=40,c=30)




# keyword only 

def sample (a,b,*,c,d):
    print(a,b,c,d) 

sample(10,20,d=40,c=30)
sample(10,20,d=40,c=30)

# lambda 
    # anonymous function 
    # small

Syntax: lambda arguments:expression 
note: automatically retuned 

# normal 
def add(a,b):
    return a+b 

print(add(10,20))

-------------------

add = lambda a,b : a+b
print(add(10,20))

mul =lambda x:x*x

print(mul(5))

high= lambda a,b: a  if a>b else b


print(type(high))
print(high(10,20))
print(high(50,20))


num=lambda x: "Even" if x%2==0 else  "Odd" if 0 else "not a number" 
print(num(5))
print(num(8))



# recurrsion
# function call itself
#5! = 5*4*3*2*1

def factorial(n):
    if n==1:
        return 1 
    return n *  factorial(n-1)

print(factorial(5))

Execution 

# Phase 1: Winding Down (Pausing to wait for smaller answers)

# Python pauses each function call in memory (the call stack) until it hits 1.
# 1. factorial(5) pauses and waits for 5 * factorial(4)
# 2. factorial(4) pauses and waits for 4 * factorial(3)
# 3. factorial(3) pauses and waits for 3 * factorial(2)
# 4. factorial(2) pauses and waits for 2 * factorial(1)
# 5. factorial(1) hits the base case and immediately returns 1

# Phase 2: Unwinding Back Up (Multiplying the returned values)

# Once factorial(1) returns 1, each paused function finishes its math in reverse order.
# 1. factorial(2) calculates 2 * 1 and returns 2
# 2. factorial(3) calculates 3 * 2 and returns 6
# 3. factorial(4) calculates 4 * 6 and returns 24

# higher order function (map,reduce,filter)

map => built in function 
Syntax: map(function,iterable)

a=[1,2,3,4]
res=[]
for i in a:
    res.append(i*2)

print(res)


a=[1,2,3,4]

result=list(map(lambda x: x*2,a))

print(result)

a=('apple','orange','banana')
res=tuple(map(lambda x:x.upper() ,a))

print(res)

a=(1,2,3,4)
res=list(map(str,a))
print(res)


a=['a','b','c','d']
print(list(map(str.upper,a)))

a=["10","20","30","40","50"]
print(list(map(int,a)))

fruits=["Guava","Custard Apple","avagado"]
print(list(map(len,fruits)))


lst=[i for i in range(1,10)]

fltr=list(filter(lambda i:i%2==0 ,lst))
print(fltr)

fruit="pineapple"
print(list(filter(lambda i : i in "aeiou",fruit)))
print(list(filter(lambda i : i not in "aeiou",fruit)))


reduce

1,2,3,4,5

0+1 => 1
1+2=> 3
3+3=> 6
6+4=> 10
10+5 => 15 

import functools as f

lst=[1,2,3,4,5]
r=f.reduce(lambda a,c : a + c ,lst)
print(r)


# generator

def fname():
    yield 1
    yield 2
    yield 3 

f=fname()
print(next(f))
print(next(f))
print(next(f))

zip()

name=["apple","orange","banana"]
color=["red","orrange","yellow"]
price=[300,200,100]

print(list(zip(name,color,price)))



# take the min match count
name=["apple","orange","banana"]
color=["red","orrange","yellow"]
price=[300,200,100,400 ]

print(list(zip(name,color,price)))

iter
----


my_list=['python','java','php']
a=iter(my_list)

print(next(a))
print(next(a))
print(next(a))
print(next(a))


print(type(10 / 2).__name__)
print(type(10 // 2).__name__)

print(isinstance(True, int))
print(True + 5)

a = [10, 20]
b = a
b.append(30)
print(a)

a = (10, [20, 30])
a[1].append(40)
print(a)

a = {1, True, 1.0, 2}
print(len(a))


11. What is the output?
print(bool("False"))
print(bool(" "))
print(bool(""))


x = "Python"
print(x[-2])
print(x[1:5:2])


13. What is the output?
print(not 0 == False)



22. Identify the problem.
age = int("25.5")
print(age)


23. What happens here?
value = float("")
print(value)


24. Identify the error.
x = "10"
y = 5
print(x + y)

numbers = [10, 20, 30]
result = numbers.append(40)
print(result)

x = 10
if x == 10:
    print("Equal")

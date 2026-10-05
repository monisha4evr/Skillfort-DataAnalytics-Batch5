Function : 
    Reusable Block of Code to Perform some Specific Task 

Syntax: 

function Declaration 

def functionname():
    #statement

Function Calling 
functionname()


def greet():
    print("Hi Welcome to Python Function")

greet()


Types: 
1. built-in Function 
2. User defined Function
3. Lambda Function 
4. recursion Function

1 . buit-in Function 
print()
input()
len() 



User defined Function 

1. argument 
2. parameter 
3. return


argument - actual value 

def add():
    pass
add()


def add():
    a=10
    b=20
    print(a+b)
add()
add()
add()
add()


def add(a,b): # parameter - alias variable
    print(a+b)

y=45
r=90
add(y,r)

add(10,20) # argument

a=50
b=30
add(a,b)

z=90
e=10
add(z,e) 


return 
------
    it returns value back to the Function 



def sub(q,w):
    print(q-w)

sub(10,6)


def sub(q,w):
    return(q-w)

s=sub(10,6)

print(s+10)


Function Type: 
------
1. without argument without return
2. without argument with return 
3. with argument without return 
4. with argument with return 


1. without argument without return

def multiply():
    a=10
    b=20
    print(a*b)

multiply()

2. without argument with return 

def multiply():
    a=10
    b=20
    return(a*b)

print(multiply())

def multiply():
    a=10
    b=20
    return 
    print(a*b)

print(multiply()) # None


3. with argument without return 

def multiply(a,b):
    print(a*b)
multiply(12,5)

4. with argument with return 

def multiply(a,b):
    return(a*b)

result=multiply(5,9)
print(result)


# argument Types:

1. positional Argument 
2. Keyword / named Argument 
3. Default Argument 
4. Arbitary Argument 


1. positional Argument 


def add(a,b):
    print(a,b)

add(10,20)

def add(a,b):
    print(a,b)

add(5,10,15)  #  add() takes 2 positional arguments but 3 were given


2. Keyword / named Argument 



def add(a,b):
    print(a,b)

add(b=5,a=10) 


def display(a,b,c):
    print(a,b,c)

display(10,c=5,b=25)

def display(a,b,c):
    print(a,b,c)

display(10,c=5,a=25) # TypeError: display() got multiple values for argument 'a'

def display(a,b,c):
    print(a,b,c)

display(c=5,a=25,10) # SyntaxError: positional argument follows keyword argument (tempCodeRunnerFile.py, line 4) 


Positional Arguments Only:


def display(a,b,c,/):
    print(a,b,c)

display(10,20,30)

def display(a,b,c,/):
    print(a,b,c)

display(10,20,c=30) # TypeError: display() got some positional-only arguments passed as keyword arguments: 'c'

def display(a,b,/,c):
    print(a,b,c)

display(10,20,c=30) 


# Keyword arguments only:

def display(a,b,*,c):
    print(a,b,c)

display(10,20,c=30) 

def display(a,b,*,c):
    print(a,b,c)

display(10,20,30) # TypeError: display() takes 2 positional arguments but 3 were given

def display(a,b,/,*,c):
    print(a,b,c)

display(10,20,c=30) 


3. Default Argument 

def display(a,b,c):
    print(a,b,c)

display(10,20) #TypeError: display() missing 1 required positional argument: 'c'

def display(a,b,c="user"):
    print(a,b,c)

display(10,20,"Govarthan")
display(10,20)

4. Arbitary Argument 

* -> positional (Store rest of the element in single Variable) -Packing
** -> keyword

def display(a,*b):
    print(a,b)
    c,d,e=b
    print(c,d,e)

display(10,20,30,40)


def display(a,**b):
    print(a,b)

display(a=10,e=20,c=30,d=40)





Lambda Function 

- Singleline Expression 
- Anonymous Function
Syntax: lambda arguments: expression 

- map
- filter 
- reduce 
- zip 

a=lambda a,b:a+b 
print(a(10,40))


def sqr(numbers):
    for num in numbers:
        num=num*2
        print(num)
    
sqr([2,4,6])

a=lambda a:a*2 
print(a(10))


Syntax:
map(function,iterable)

a=[10,20,30]
print(list(map(lambda i:i*2,a)))

Filter => Filter Based On Condition

Syntax: filter(function,iterable)

a=[15,20,31,41,36,20,34]

def samp(n):
    newss=[]
    for i in n:
        if i%2==0:
            print(i)


filter(samp(a),a)

from functools import reduce
num=[10,20,30,40]
res=reduce(lambda a,b:a+b,num)
print(res)












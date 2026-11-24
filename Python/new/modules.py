Modules 
 -   python file that contains pre-written code 
 -   function, variables,classess 
 -   we can import and reuse in another python program 

Types: 
1. Built-in 
2. user-defined 

import math 
print(math.sqrt(25))
print(math.factorial(5))
print(math.ceil(11.5))
print(math.ceil(11.1))
print(math.floor(11.5))
print(round(11.1))
print(round(11.5))

import random 
print(random.choice(["python","Java","SQL"]))
print(random.randint(1,10))

import datetime
current = datetime.datetime.now()
print(current)
print(current.year)
print(current.month) 

import statistics
marks=[80,90,70,85,95]
print(statistics.mean(marks))
print(statistics.median(marks))
print(statistics.mode(marks))


different ways to import 

1. import entire module
import math
print(math.sqrt(25))

2. import specific function

from math import sqrt
print(sqrt(25))

from math import sqrt,factorial
print(sqrt(25))
print(factorial(25))

3. import with alias 

import math as m 
print(m.sqrt(25)) 

Type 2: 
user defined Module 


import calculation as c 
print(c.add(20,50))
print(c.multiply(20,5))

PYPI => python Package Index 
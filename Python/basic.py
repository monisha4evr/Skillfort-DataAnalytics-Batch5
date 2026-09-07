# input and output Operation
# output Operation

# print("Hello Word")

# a_val=50
# print("a value is : ",a_val)

# print(f"a value is :{a_val} ")

# input("Enter Your Name")
# print(input("Enter Your Name"))


# Below code get username from the user
name=input("Enter Your Name")
print(name)


Variable
--------

1. allow alphabets(a-zA-Z),0-9 ,_
2. cannot start with number 
3. can start with _(underscore)/Alphabet 
4. cannot accept space between Variables name
5. Reserved keyword 


firstName 

first_name 

frist name wrong


eg: price 

12price  wrong

_price

input  wrong

a=50
b=10
a="apple"

print(a+b)
print(a+b)
print(a+b)
print(a+b)
print(25+20)
print(24+22)


Datatype:

int 
----
type() # to find the type of value

a=10 
print(type(a)) # <class 'int'>
a=-10 
print(type(a)) # <class 'int'>
a=+10 
print(type(a)) # <class 'int'>

float : 
------- 
a=10.5 
print(type(a)) # <class 'float'>

a=-10.5 
print(type(a))

str: 
# sequence of character 

a="flower"
print(type(a)) # <class 'str'>
a='flower'
print(type(a)) # <class 'str'>

bool
a=True  
print(type(a)) # <class 'bool'>
a='true'
print(type(a)) # <class 'str'>

collection 
list - [] - hetrogenous , 
1. ordered ,
2. mutable ,
3. allow duplicate 
eg: 
    a=[1,5.6,'flower']
    print(type(a)) # <class 'list'>


a=[1,2,3,4,5]
print(a)
print(id(a))

tuple
() ,hetrogenous
1. ordered
2. immutable
3. allow Duplicate

a=(1,2,3,4)
print(id(a))

set 
{1,2,3,4}
- unordered 
- cannot allow duplicate 
- mutable
a={1,2,2,3,4,4,5}
print(a)

dict 
key- value 
        {k:"v"}
        - key unique 
        - value allows Duplicate .
        - not iterable 


a={"name":"Apple","color":"Red"}
print(a)

print(a['name'])


immutable :

int 
str 
bool 
None
float
tuple 

mutable:

list
set 
dict



immutable : 

a=10
print(id(a))
b=10
print(id(b))
a=15
print(id(a))
print(id(b))


a=(1,2,3,4)
b=(1,2,3,4)

print(id(a))
print(id(b))



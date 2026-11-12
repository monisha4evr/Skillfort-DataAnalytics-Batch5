
a=10
print("Hello world")

print("My number is ",a)
print(f"My number is {a}")

data types: 

integer -> int 
float


a=-10.50
print(type(a))
print(a)

a="apple"
print(type(a))
print(a)

a=True 
print(type(a))
print(a)


a="" 
print(type(a))
print(a)

Collection:
--------------
1. list 
2. tuple 
3. set 
4. Dictionary (dict)


list : 

1. denoted by []
2. ordered 
3. mutable
4. allow duplicate 
5. hetrogenous

a=[1,2,3,4,5,5,5]
print(a)
print(type(a))


a=[1,1.2,"apple",True]
print(a)
print(type(a))



Tuple:
------ 
1. denoted by ()
2. ordered 
3. immutable
4. allow duplicate 

a=(1,2,3,4,5,5)
print(a)
print(type(a))


b=(1)
a=(1,)
print(a)
print(type(a),type(b))

set:
------ 
1. denoted by {}
2. unordered 
3. mutable
4. not allow duplicate 

a={1,2,2,2,3,4,5,6,7,8}
print(a)
print(type(a))


dictionary:
------------

: key-value pair 
1. denoted by {}
2. ordered 
3. mutable
4. key- unique , value - allow duplicate   


a={
    "name":"apple",
    "color":"red",
    "price":"30",
    "price":"300"
}

print(a)
print(type(a))


data type -> object 

1. numeric  -> int, float , complex 
2. sequence -> str , list, tuple 
3. set -> {}
4. map -> dict 
5. others -> bool,NoneType (None)


mutable: (changable)
List, set,dict 

immutable : 
tuple,int,str,float 








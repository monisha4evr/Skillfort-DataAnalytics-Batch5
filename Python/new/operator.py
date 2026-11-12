Types
1. Arithmetic operator (+,-,*,/,//,%,**)
2. Asignment operator 
3. Comparision 
4. Logical 
5. Membership Operator ()
6. Identity Operator 
7. Bitwise Operator


1.Arithmetic Operator: 
a=15
b=2 

print("add",a+b)
print("subtract",a-b)
print("multiply",a*b)
print("Divide",a/b)
print("Floor Division",a//b)
print("modulus",a%b)
print("exponential",2**3)

2. Assignment Operator 

assign value to variable 

+=,-=,*=,/=


a=10 
print(a)
a+=5       
print(a)  

3. Comparision Operator 

== equal to 
!= not eual to 
> Greater than
< Less than
>= Greater than or equal to
<= less than or equal to


a=10
b=10

print(a>=b)

4. Logical Operator

and , or , not 

age=20
has_id=False 

print(age>=18 and has_id)
print(age>=18 or has_id)

has_id=False 
print(not has_id)


print(20 and 10) 

5. Membership Operator

in, not in

fruits=["apple","orange","Banana"]

print("apple" not in fruits)

name="pyThon"
print("t" in name)

num=str(123)
print("2" in num) 


6. Identity Operator 

is , is not 

a=10 
b=20 
print(id(a))
print(id(b))

print (a is b) 

a="Apple"
b="apple"

print(id(a))
print(id(b))
print (a is b) 


a=(1,2,3)
b=(1,2,3)
print(id(a))
print(id(b))
print (a is b) 


a=[1,2,3]
b=a 

print(id(a))
print(id(b))
print (a is b) 


a=[1,2,3]
b=a.copy()

print(id(a))
print(id(b))
print (a is b) 

7. Bitwise Operator

and (&) or(|) not (~) xor (^)

a=5
b=7
print(a&b)

5= 0101
7= 0111
-------
   


a=5
b=7 
print(a^b)

a=5 
print(bin(a))
print(~a)

>> 

<< 



0001      01

010100
a=5
print(a>>2)
print(a<<2)


0011     1
01110
a=7
print(bin(7))
print(a>>1)
print(a<<1)


a='apple'
b="banana"
c=""" Python 
is 
Interesting

"""

print(a,b,c)

a="apple"
print(a.upper())

b="Banana"




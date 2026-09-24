Operators 

Special Symbol 
- combination of Symbols and keywords 
- used to Perform some Operation 


Types of Operators: 

1. Arithmetic Operator 
2. Assignment Operator 
3. Comparision Operator 
4. Logical Operator 
5. Identity Operator 
6. Membership Operator 
7. Bitwise Operator 


1.Arithmetic Operator: 
----------------------

- used to Perform Mathemetical Calculation 
addition  (+)
subtraction (-)
multiplication (*)
division (/)  10.5 - quotent
modulo-division (%) -  remainder
floor Division (//)  10
Exponentiation (**)

Example:

a=10
b=20 
c= a+b 
print(c)
print("Subtraction",b-a)
print("Multiplication",a*b)
print("Division",15/2)
print("Modulo Division", 15%2)
print("floor Division",15//2)
print("Exponentiation",2**4)


2. Assignment Operator 

a=5
print(a)
a+=2  # (a=a+2)
print(a)
a*=3 (a=a*3)
print(a)

3. comparision Operator: 

Equal to  '=='
Not equal to '!='
Greater than '>'
Less than '<'
Greater  than or equal to '>='
Less than or equal to '<='

a=10 
b=10
print(a>b)
print(a==b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)
print(a!=b) # False

4. Logical Operator 

-  Check two or more Condition

and - all true  -> True  orelse False
or - 
not - 

0=> False 
1=> True 

and 
----
False True  -> False 
True  True  -> True 
True  False -> False 
False False -> False 

or 

False True -> True 
True  False -> True 
True  True -> True 
False False -> False

not 
true -> False 
false -> True 


age = 12
print(age>=18 and age<=60 )

70>=18 -> True
70<=60 -> False

12>=18 -> False -> false 


age = 12
print(age>=18 or age<=60 )

12>=18 -> False 
12<=60 -> True 

age=18
print(not age>=18)

5. Identity Operator 
is , is not 

a=10 
b=15

a=[1,2,3,4]
b=[1,2,3,4]

print(a is b)
print(id(a),id(b))


a=[1,2,3,4]
b=a

print(a is b)
print(id(a),id(b))

a=[1,2,3,4]
b=a.copy()

print(a is b)
print(id(a),id(b))

a=[1,2,3]
b=[1,2,3]

print(a is b)
print(id(a))
print(id(b))

c=a
print(a is c)
print(id(a))
print(id(c))

a=10
b=10
print(a is not b)


6. Membership Operator 
-----------------------

in  - value  Present
not in - value  not Present

a=[1,4,7,3,8]
print(4 in a)
print(4 not in a)
print(5 in a)
print(5 not in a)

7. Bitwise Operator 
& - AND
| - OR
~ - NOT 
^ - Xor (same 0 different - 1)
>> - right Shift
<< - Left Shift

a=5 #- 0101
b=3 #- 0011
# ------------
        

a=7
b=5
print (a&b)

a=5 
print(a>>2)

# 5=> 0001     01

a=7 
print(a>>2)
print(a<<2)

print(bin(17)) # to convert binary number 
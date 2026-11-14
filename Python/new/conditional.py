Conditional Statement : 

    take decision Based on Condition

type: 
if 
if else 
if -elif -else 
nested if 


if 

Syntax: 
--------

if condition : 
    # statement 

age=12

print("Age is :",age)
if age==18 :    #12==18=> False
    print("Age is 18")
print("Example for If Condition")


if else
-------
checks the condition ,if true it executes True Block otherwise it executes else Block

Syntax: 
-------
if condition : 
    # True Statement 
else :
    # False Statement

username="apple"
password="apple123"

if password=="apple123" and username == "apple":
    print("Successfully Logged in")
else:
    print("Invalid Credential")

if ... elif ..else 
-------------------
>=90 => "S grade"
90< and >=80 => "A grade"
70> => "B grade"

mark=96
if mark >=90:
    print("S Grade")
elif mark<90 and mark>=80 :
    print("A grade")
else:
    print("B grade")

nested if :
------------

# syntax: 
# if condition:
#     if condition:
#         Statement

# else:
#     statement

age= 19
has_license =True 

if age >=18 :
    if has_license:
        
        print("Eligible to Drive")
    else:
        print("Buy License")
else:
    print("Age Restricted")


if condition :
    if condition:
        Statement
    if condition:
        statement


things="fruits"
if True:
    if things=="veg":
        print("brinjal","tomato")
    if things=="fruits":
        print("apple","orange")


Match case:
----------- 

ATM 
1. Check Balance 
2. withdraw Money 
3. Deposite Money 
4. Exit 

choice=9
match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw Money")
    case 3:
        print("Deposite Money")
    case 4: 
        print("Exit")
    case _:
        print("Invalid Choice ")

task 

weekday/weekend 
operator => add and print the output 


+ =>(Mathematical operations)


age=18
if age>18 :
    print("Age is Grater than 18")
else :
    print("Age is Lesser ")
    


Ternary Operator:
----------------- 
Syntax: variable = value_if_true if condition else value_if_false 

age=20
print("Age is Grater than 18" if age>18 else "Age is Lesser " )

 


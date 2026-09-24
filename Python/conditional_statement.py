Conditional Statement 

making Decision in program based on condition 

if 
nested if
if else 
elif 


if conditon 
------------
execute if Condition True
Syntax 

if condition :
    # statement

age=12

if age>18:
    print("Eligible")


age=19
print("your Age is ",age)
if age>18:
    print("Eligible")

print("example for if statement")

if ... else 
If condition True execute if block otherwise it execute else block 

Syntax:
if condition :
    # true block 
else : 
    # false block


user_name ="siva"
password="siva@1234"
if user_name=="siva" and password=="siva@1234":
    print("Successfully Logged In")
else :
    print("invalid Credential")


if ... elif ... else 
used to check more condition 

Syntax: 

if condition :
    # statement 
elif condition :
    # statement
elif conditon :
    # statement
else :
    # statement 

total=80
if total>=90:
    print("A grade")
elif total >= 80 and total <=89:
    print("B grade")
elif total >=70 and total <=79:
    print("C Grade")
else:
    print("D grade")

# Biggest of 3 numbers
a=70 
b=45 
c=80

if a>b and a>c :
    print(" a is Bigger")
elif b>c:
    print("B is Bigger")
else:
    print("C is Bigger")

Nested if:

age =18
voter_id=False

if age>=18:
    if voter_id:
        print("Allowed to Vote")
    else:
        print("Voter id Needed")
else:
    print("Age must be above 18")

if (1,2):
    print("if block")
else:
    print("Else block")
# truthy falsy
Falsy: 0 , None , False , "",[] empty collection


ternary operator : 

if condi:
    statem 
else : 
    statement

syntax:
value_if_true if condition else value_if_false 

a=10 
if a%2==0:
    print("Even")
else :
    print("Odd")

a=12
print( "Even" if a%2==0 else "Odd")












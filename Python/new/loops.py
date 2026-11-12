Loops
- Execute a block of code repeatedly until a particular Condition is Satisfied

Types:

for and while 
--------------
range()
syntax: 
range(start, stop, step) 


range(5)

for i in range(5):
    print(i)

print("Starting Loop")
for i in range(1,6):
    print("welcome")
    print(i)
    print("End")

print("End of Loop")


fruits=["apple","orange","banana"]
for i in fruits:
    print(i)

fruit={
    "name":"apple",
    "color":"red"
}

for i in fruit:
    print (i)

for k,v in fruit.items():
    print("key is",k)
    print("value is",v)

for i in fruit.keys():
    print(i)

for i in fruit.values():
    print(i)


while loop 
- it runs as long as Given Condition is True

Syntax: 
initalization 
while condition :
    statement
    incr/decre 


i=1
while(i<=5):
    print(i)
    i+=1

i=5
while(i>=1):
    print(i)
    i-=1

Loop Control Statement 
----------------------
1. break - stop the loop
2. continue - Skip the Current Iteration
3. pass - Do Nothing

for i in range(1,6):
    if i == 3:
        break
    print(i)

for i in range(1,6):
    if i == 3:
        continue
    print(i)

for i in range(1,6):
    pass
print("Hello")

a=153
351 

Task 1 : reverse the Number 
Task 2 : sum of digit 

# Nested for loop
# ------------------
one Loop inside another Loop


for i in range(1,4):   # [1,2,3]
    for j in range(1,4): #[1,2,3]
        print(i,j)

execution :
------------
i=1 
    j=1   # 1 1
    j=2   # 1 2 
    j=3   # 1 3 
i=2 
    j=1  # 2 1
    j=2  # 2 2
    j=3  # 2 3 
i=3
    j=1   # 3 1 
    j=2   # 3 2 
    j=3   # 3 3 

output
* * *
* * * 
* * * 


for i in range(1,4):   # [1,2,3]
    for j in range(1,4): #[1,2,3]
        print("*",end=" ")
    print()


for i in range(1,4):   # [1,2,3]
    for j in range(1,4): #[1,2,3]
        print(i,end=" ")
    print()

1 1 1 
2 2 2 
3 3 3 

for i in range(1,4):   # [1,2,3]
    for j in range(1,4): #[1,2,3]
        print(j,end=" ")
    print()

1 2 3 
1 2 3 
1 2 3 

1
12
123

for i in range(1,4):
    for j in range(i):
        print("*",end="")
    print()

#       1
#     1 2
#   1 2 3


# A, b, c
# ----------

print("12"*5)

a=["apple"]
print(a*5)

for i in range(1,5):
    print("*"*i)

for i in range(5,0,-1):
    print("*"*i)

n=6
for i in range(1,n):
    print(" "*(n-i) + "*"*i)


# Comprehension:
# simple way to create a new collection 

# Types of Comprehension:
# -----------------------
1. list Comprehension 
2. Dictionary comprehension 
3. set Comprehension 

# norwal way
a=[1,2,3,4,5]
b=[]

for i in a:
    b.append(i*2)

print(b)

# List Comprehension
# Syntax: [expression for variable in iterable]

a=[1,2,3,4,5]
print([i*2 for i in a])
print([i*2 for i in a if i%2==0]) 


# 2.Dictionary Comprehension
# ---------------------------
num=[1,2,3,4,5]
print({i:i*2 for i in num})

# 3. set comprehension
# ---------------------------
b=[1,2,3,4,5]
c={i*2 for i in b}
print(c)
print(type(c))


num={1,2,3,4,5}
c={i:i*2 for i in num}
print(c)
print(type(c))
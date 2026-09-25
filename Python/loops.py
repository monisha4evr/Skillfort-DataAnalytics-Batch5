
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")

# print(1)
# print(2)
# print(3)


# To avoid and simplied the repetative task 


# 1-10
# Syntax: 
# range(start,end,step)


# for i in range(1,11):
#     print(i)

# 2 type:
# for - 

# while - 


# 10 - 1

# for i in range(10,0,-1):
#     print(i)

# a=[10,20,30,40]
# for i in a:
#     print("welcome")
#     print(i)
#     print("hi")
# print("Example for Loop")


# a=(2,4,6,8)
# for i in a:
#     print(i)


# for i in range(1,11):
#     if i%2 == 0:
#         print(i)

# for i in range(1,11):
#     if i%2 == 0:
#         print(i)
#     else:
#         print("odd")

# a="123"
# for i in a:
#     print(i)

# a="flower"
# for i in a:
#     print(i)

# a={12,24,54,69}
# for i in a:
#     print(i)

# a={
#     "name":"apple",
#     "color":"red"
# }

# for i in a:
#     print(i)

# for i in a.values():
#     print(i)

# for k,v in a.items():
#     print(k,v)

# a=[]
# for i in range(1,11):
#     if i%2==0:
#         a.append(i)
# print(a)

# total=0
# for i in a:
#     total+=i

# print(total)


# # while:
# # ------

# syntax: 
# initialization 
# while condition:
#     statement
#     incre/decre 


# example :

# i=1
# while i<=10:
#     print(i)
#     i+=1 

pin=""
while pin !="1234":
    pin = input("Enter Pin") 


a=123

print(a%10)

1st =>
r = % 3    => 3
a = 123 // 12 

2=> 
a=12 
a%10 => 2    => 2
a//10 =>  1

3=> 1
a%10 => 1    => 1
a//10 => 0


print(1//10)
print(1%10)

Jumping Statement: 

1. break # break the loop
2. continue # skip the Current iteration
3. pass  # to avoid Error


for i in range(11):
    if i==5:
        break
    print(i)


for i in range(11):

    if i==3:
        continue
    print(i)


for i in range(11):
    pass


*
**
***
****
*****


print("*"*2)


for i in range(1,6):
    print("*"*i)


*****
****
***
**
*

for i in range(5,0,-1):
    print("*"*i)

   *
  **
 ***
****

for i in range(1,6):
    print(" " * (6-i)+ "*"*i)
 
 
a= " "
b= "*"
print(a+b)


*****
 ****
  ***
   **
    *

for i in range(5,0,-1):
    print(" "*(5-i) + "*"*i)

Nested Loop 

outer condition -> check condi 
    inner loop -> loop until condition Fail 
outer loop -> cond check 
    inner loop -> loop untill condition fail 
outer loop -> condition fail 


for i in range(1,6):
    print("Outer",i) 
    for j in range(1,6):
      print(j, end=" ")
    print()




1234
1234
1234
1234


execution 

i=[1,2,3]
j=[1,2,3]

i=1 
    j=1 2 3
    i=1 1 1
i=2
    j= 1 2 3
    i= 2 2 2 
i=3 
    j= 1 2 3
    i= 3 3 3 

1111
2222
3333
4444

for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()

for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print()

# Execution:
# ----------
i=1
    j=1   1
    j=2   2
    j=3   3
    j=4   Fail 
i=2 True 
    j=1     1
    j=2 2
    j=3 3
    j=4 Fail 
i=3 
    j=1     1
    j=2 2
    j=3 3
    j=4 Fail 
i=4 Fail 

Task:
-----
1
12
123
1234

1
22
333
4444

sqr=[]
for i in range(1,6):
   sqr.append(i**2)
print(sqr)


list comprehension 

Syntax:
new_list=[expression for i in iterable]

sqr = [i**2 for i in range(1,6)]
print(sqr)

a = [1,2,3,4,5]
print(["Even" if i%2==0 else "Odd" for i in a])
print([i if i%2==0 else "Odd" for i in a])


task : 
tuplecomplrehension
dictionarycomprehension



      
    
    




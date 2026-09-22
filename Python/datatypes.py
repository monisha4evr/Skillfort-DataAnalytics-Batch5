a=10
b="banana" 
c=10.5

print(type(b))

a="10"
b=+20.5

print(type(a),type(b))


a="apple"
print(type(a))

a='banana'
print(type(a))

a="""
quick brown fox jummped over lazy dog
today is Monday
"""

print(a,type(a))


print(list(range(1,11)))
Syntax:
range(start,end,step)
print(list(range(1,10,2)))


a=None 
print(a)
print(type(a))

b=True
print(type(b))



a=[1,2,2,3,4,"apple",12.5,True]
print(a)
print(type(a))


a=(1,2,2,3,4,"apple",12.5,True)
print(a)
print(type(a))

b=[1]
print(b)
print(type(b))


b=(1,)
print(b)
print(type(b))

c={1,2,3,2,3,3,4,4,5,"apple"}
print(c,type(c)) 

c={}
print(c,type(c)) 


d= {
        "name":"orange",
        "color":"orange",
        "price":102.5
    }

print(d,type(d)) 

a=10
print(id(a))
a=20
print(a)
print(id(a))


a=10
b=10

print(id(a),id(b))


a=[1,2,3,4]
b=[1,2,3,4]

print(id(a),id(b))


a=(1,2,3,4)
b=(1,2,3,4)

print(id(a),id(b))
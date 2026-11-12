# Types:
# List  
# Tuple 
# Set 
# Dictionary 


# 1. List  
#     - Ordered 
#     - Mutable 
#     - Duplicate Allowed  

a= [1,2,3]
print(a)

# add items in List 
# 1. append  - > Add item at the end of List
# 2. extend  -> end of the List
# 3. insert 

a=[1,2,3]
a.append(4)
print(a)
a.append([5,6])
print(a)
a.append((7,8))
print(a)
a.append({9,0})
print(a)

a=[1,2,3]
b=(4,5,6)
a.extend(b)
print(a)

print(a+b)

a=[10,40,50]
a.insert(1,"20")
print(a)

a=[10,40,50]
a.insert(1,20)
a.insert(2,[20,10])
print(a)


# remove: 
a=[1,2,3]
a.remove(1)
print(a)

a=[10,20,30]
b=a.pop()
b+=10
print(b)
print(a)

a=[20,40,60]
b=a.pop(1)
print(b,a)

a.clear()
print(a) 

# copy 
a=["apple","orange"]
b=a
print(a is b)
b=a.copy()


# count  -> Number of Occurance
a=[1,2,2,1,2,2,2,2,4,5,7]
print(a.count(2))

# index ->  search and return its Position 

a=[1,2,3,4,5,5,6,6,7]
print(a.index(5)) 


sort 

a=[3,1,6,2,0,3,8]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a=["pineapple","apple","cherry","kiwi"]
a.sort()
print(a)
a=["pineapple","apple","cherry","kiwi"]
a.sort(reverse=True)
print(a)
a=["pineapple","apple","cherry","kiwi"]
a.sort(key=len)
print(a)

a=["pineapple","apple","cherry","kiwi"]
print(sorted(a))
print(sorted(a,reverse=True))
print(a)

# reverse :

a=["pineapple","apple","cherry","kiwi"]
a.reverse()
print(a) 

Tuple: 
    - Immutable 
    - ordered 
    - Duplicate Allowed 

a=(1,2,3,4,2,2,2,2)
print(a.index(2))
print(a.count(2))


set :
    - mutable 
    - duplicate not Allowed 
    - unnordered 

a={1,2,3,4,5,6,5}
print(type(a))
print(a)

a={1,2,3,4,5}
a.add(9)
print(a)

a={1,2,3,4,5}
a.update([10,20,30])
print(a)

a.pop()
print(a)
a.remove(20)
print(a)
a.discard(30)
print(a)


a={1,2,3,4,5}
a.discard(9)
print(a)
a.clear()
print(a)
a. remove(6)
print(a)

a={10,20,30}
b={10,40,50}
print(a.union(b))
print(a|b)

a={10,20,30}
b={10,40,50}
print(a.intersection(b))
print(a & b)

a={10,20,30}
b={10,40,50}
print(a.difference(b))
print(a-b)

a={10,20,30}
b={10,40,50}
print(a.symmetric_difference(b))

a={10,20}
b={10,20,30,40}
print(a.issubset(b)) # true


a={10,50}
b={10,20,30,40}
print(a.issubset(b)) # False 

a={10,50}
b={10,20,30,40}
print(b.issuperset(a))


dict 
    - Mutable 
    - ordered 
    - key is unique , value allow duplicate 

fruit={
    "name":"apple",
    "color":"red",
    "price":500
}

print(fruit)
print(fruit.get('name'))
print(fruit.keys())
print(fruit.values())
print(fruit.items())
fruit.update({"price":300,"city":"Kashmir"})
print(fruit)

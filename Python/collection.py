list
tuple 
set
dict 

list 
    - mutable 
    - ordered 
    - Duplicate allow 
    - Hetrogenous 

a=[1,2,3,4]

add :
----
append (add value at the End )
extend 
insert

a=[1,2,3,4]
a.append(5)
print(a)
a.append([6,7])
a.append((6,7))
print(a)
a.extend([8,9])
print(a)
a.insert(2,9)
print(a)

remove/delete 

1. pop()/ pop(1) # last element / index based 
2. clear() # remove full list
3. remove() # remove based on value


a=[10,20,30,40,50]
a.pop()
print(a)
a.pop(1)
print(a)

a=[1,2,3,4,2,3,4,3,2]
a.remove(2)
# a.remove(5) # it throws Error x not in list
print(a)
print(a)
print(a.pop())
print(a)
a.pop(1)
print(a)

a.clear()
print(a)

#count , len
a=[1,2,3,3,3,3,3,4,5,5,5,6,6,6,6,6,6]
print(a.count(3))
print(a)
print(len(a))

copy: 
1. assign 
2. copy()


a=[1,2,3,4]
b=[1,2,3,4]
c=a
print(id(a),id(b),id(c))


a=[1,2,3,4]
b=a
b.append(5)
print(a)
print(b)

print(id(a),id(b))

a=[1,2,3,4]
c=a.copy()
c.append(5)
print(a)
print(c)

print(id(a),id(c))


sort 
a=[5,2,8,4,1,3]
print(a)
a.sort()
print(a)
a.sort(reverse=True)  # descending order
print(a)

Task 1: ["apple","orange","Banana","gauva"]

reverse: 
--------
a=[5,2,8,4,1,3]
print(a)
a.reverse()
print(a)

index:
------
a=[1,2,3,5]
print(a.index(3))
# print(a.index(7)) => it will throw Error



tuple: 
--------
    - immutable 
    - ordered 
    - Allow Duplicate 
    - hetrogenous


a=(1,)
print(type(a))

a=(1,2,3,4,1,1,1,1)
print(a)
print(a.count(1))  # occurance
print(a.index(3))  # return index position


set
---
    - mutable 
    - unordered 
    - dont allow duplicate 


a={10,20,20,30,30,30}
print(a)

# Remove List from Duplicate
# -------------------------
a=[10,20,20,30,30,30]
print(list(set(a)))

a={1,2,3,4}
b={1,5,6}
print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))


dict 
        - Key value pair 
        - Key unique , value - allows duplicate 
        - ordered 

a={"name":"apple","color":'red'}
print(a)

a['price']=102.5
print(a)
a['color']='Green'
print(a)

a = {"name": "apple", "color": "red"}

print(a.keys())
print(a.values())
print(a.items())
print(a.get("name"))
#print(a["price"])       # KeyError if price doesn't exist
print(a.get("price"))   # None if price doesn't exist
a.update({"price": 100})

print(a)
a.popitem()
print(a)
a = {"name": "apple", "color": "red"}

a.setdefault("price", 100)

print(a)

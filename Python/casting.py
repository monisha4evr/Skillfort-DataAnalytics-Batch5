# Type casting:
# ------------- 


# => convert one data type into another data type


a = int(input("Enter a Value"))
b = int(input("Enter b Value"))
print("A",type(a))
print("b",type(b))
c=a+b
print(c)

# 2 Type: 
# 1. implicit (Automatic conversion)
# 2. Explicit (Manual Conversion)

# Explicit:
# ----------

int()
float()
str()
list()
tuple()
set()


a=12.5
print(type(a))
print(type(int(a)))

a='12'
print(type(a))
print(type(int(a)))

# str to int
a="flower"
print(type(a))
print(type(int(a)))

a="12flower"
print(type(a))
print(type(int(a)))

a="*10"
print(type(a))
print(type(int(a)))

a="+10"
print(type(a))
print(type(int(a)))

a="-10"
print(type(a))
print(type(int(a)))


a = 10
b = 12.5

print("A",type(a))
print("B",type(b))
c=a+b
print(c)
print("C",type(c))
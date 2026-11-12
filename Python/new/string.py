- sequence /collection of character 
- data type: str 

- we can define string by enclosing single,double , Triple quotes 


a='apple ' 
b="banana"
c=''' Today is Thursday
we are Learning Python String '''

# Command Lines
    # 1. single Line #
    # 2. Multiline ''' ''' 

print("Apple")
''' print("Orange") '''
print("Banana")



a="I have Lega's pencil"
a='I have Lega\'s "pencil" '
print(a)

# indexing and Slicing
# indexing

a="apple"
print(a[4])

a="the Quick Brown fox Jumped over Lazy Dog"
a="apple "
print(len(a))
print(a[::-1])
# Syntax:
# var_name[start:end:steps]

print(a[10:15])
print(a[27:31])
print(a[:])
print(a[10:])
print(a[:10])

print(a[-8:-4])
print(a[-4:])
print(a[::2])

a="1234567890"
print(a[::3])
print(a[::-1])

a="apple"
b="banana"
print(a+" "+b)

# caseConversion:

a="apple"
print(a.upper())
print("JASMINE".lower())
print("camel is desert animal".capitalize())
print("camel is desert animal".title())
print("Camel is desert animal".swapcase())

# search 
print("Hello World".find('W')) # Return its Index Position
print("Hello World".index('W')) # Return its Index Position
print("Hello World".find('P')) # Return its Index Position
print("Hello World".index('P')) # Return its Index Position
print("Hello World".count('l')) # Count the Occurance
print("Hello World".startswith('H'))
print("Hello World".endswith('d'))


# Remove Spaces
print(" Hello World ")
print(" Hello World ".strip())
print(" Hello World ".lstrip())
print(" Hello World ".rstrip())
print("123SOQ123".removeprefix('123'))
print("123SOQ123".removesuffix('123'))

# Replace
print("Hello World".replace("World","Arifa"))

# Split
print("red,blue,green,orange,yellow".split(","))
print("red,blue,green,orange,yellow".rsplit(",",2))

# partition 
print("Sakthi@gmail.com".partition('@'))
print("deepal.1510@gmail.com".partition('.'))
print("deepal.1510@gmail.com".rpartition('.'))


#checking
print("123".isnumeric())
print("123".isalnum())
print("apple@".isalnum())
print("apple ".isalnum()) 


#Aligment
print("hello".center(10,"0"))
print("hi".center(10," "))
print("hi".ljust(10,"0"))
print("hi".rjust(10,"0"))
print("hi".zfill(10))

a="apple"
b="banana"
print(f"Fruit Name is {a}")

#old version
print("Fruit Name is {}".format(a))
print("Fruit Name is {},{}".format(a,b))

a=['apple','orange','banana']
print(" @ ".join(a))


a="apple"
print(a[::-1])









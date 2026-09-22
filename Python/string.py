
String :
--------

sequence of Character 

denoted by  
    # signle quote ''  => Single Line
    # douple quote ""  => Single Line
    # triple quote """ """ ,''' ''' => Multiple Line accept

a='flower'
print(a)
print(type(a))

a="Flower"
print(a)
print(type(a))

a="""
the 
quick
brown
fox
jumped
over
lazy
dog
 """
print(a)
print(type(a))


a='''
Rainbow are
very colorful
'''

print(a)
print(type(a))


a='pleasant Morning '

print(a)

a="cant't"



a="i can't do this"
print(a)


a='i can\'t do this'
print(a)
a="i can\"t do this"
print(a)

slicing
-------


a="i am learning Python"
# i am learning Python
# 012345678910111213141516171819
print(a[5])
print(a[12])
print(a[19])


syntax: [start:end(exclusive):step]
    [:]
start-> Optional starting index 
end -> Optional ending index (n+1) 
step -> Optional - default (+1)

a="i am learning Python"
print(a[5:13]) # starting index 5 upto 12 index
print(a[14:20]) 
print(a[5:20])
print(a[5:20:2])
print(a[5:20:3])
print(a[:])  
print(a[0:])
print(a[:4])

# reverse 
a="she is very beautiful"


print(a[::-1])
print(a[:-1])
print(a[-9:])


flower
r -1
e -2
w -3
o -4
l -5
f -6


a="flower are Beautiful"
print(a.isalpha())
print(a.endswith('e'))
print(len(a))
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.count('a'))

# search
a="flower are Beautiful"
print(a.find('a')) # it print the first occurance 
print(a.find('y'))  # it returns -1 if letter not found
print(a.index('a'))
print(a.index('y')) # it throw error if letter not found

# startswith
a=" flower are Beautiful"
print(a.startswith(" "))
print(a.startswith('f'))
print(a.startswith('l'))
print(a.endswith('l'))
print(a.endswith('f'))


0000000001


a="flower"
print(a.zfill(10))

a='12'
print("prd"+a.zfill(5))

a="Flower"
print(a.islower())


a="guru"
b="narayanan"

print(a+' '+b)

a="apple" 

print(a*5)

a="10"
b="20"
print(a+b)

print([1,2,3,4]*5)
print([1,2,3,4]+5)


text="i,am,learning,python"
print(text.split(','))

text="Arifa@gmail.com"
print(text.split('@'))


a=['Arifa', 'gmail.com'] 
res="@".join(a)
print(res)





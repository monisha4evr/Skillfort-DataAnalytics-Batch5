Regex  (Regular Expression)
- pattern used to search , find,extract, validate 

import re 
re.match() => Check pattern 
re.search() => find first match  
re.findall() => return all matches in the list 
re.split() - splits string based on pattern 

[a-zA-Z] => small/caps alphabet
[abcd] => a or b or c or d
[0-9] => any digit 
\d => any digit 
\D => non-digit 
\w =>letter,digits,underscore 
\s => whitespace 

Quantifiers
-----------
^ start of the string 
$ End of the string
*  zero or more 
+  one or more
? zero or one 
{10} exactly 10 times 
{2,5} 


import re 

text="Dhoni is Retired at the age of 45"
result=re.findall(r'\d+',text) 
print(result)


import re 
text="123python programming45664"
res=re.findall(r'\D+',text)
print(res)

import re 
text = "Python is easy. I Love Python"
print(re.match("Python",text))
print(re.search("Python",text))

import re 
text = "python is easy. I Love Python"
print(re.match("Python",text))
print(re.search("Python",text))


import re


def is_valid_email(email: str) -> bool:
  pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
  return bool(re.fullmatch(pattern, email))


# Examples
print(is_valid_email("user@example.com"))  # True
print(is_valid_email("first.last+tag@sub.domain.co.in"))  # True
print(is_valid_email("invalid-email@.com")) 


decorator:
-----------

- special function 
- extend the functionality without modifying the origal code

denoted by @ 


def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

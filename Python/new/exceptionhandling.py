a="apple"
print(a.index("O")) # ValueError: substring not found

try  : block we except error 
except : catch the error
else : execute when no error 
finally : execute Everytime 
raise : custom error 

exception 
1. generic Exception
2. specific Exception:  ValueError,TypeError,ZeroDivisionError

# 1. TypeError => 

a="10"
b=20
print(a+b)  # TypeError: can only concatenate str (not "int") to str
print("Welcome to Python Programming")
print("learning python is Easy and interesting")


try :
    a="apple"
    print(int(a))
    print("welcome")
except ValueError:
    print("Cant convert into int from String")
else:
    print("No Error")
finally:
    print("I will run Everytime")


try:
    a=0
    if a>0 :
        print("a is greatter than 0",a+"20")
    else:
        print(10/a)
except ZeroDivisionError,TypeError:
    print("Eror occured")

try:
    a=10
    if a>0 :
        print("a is greatter than 0",a+"20")
    else:
        print(10/a)
except ZeroDivisionError:
    print("Zero division occured")

except TypeError:
    print(" unsupported operand type(s) for +: 'int' and 'str' ")
except Exception as e:
    print(e)




try:
    a=10
    if a>0 :
        print("a is greatter than 0",a+"20")
    else:
        print(10/a)

except Exception as e:
    print(e)
except ZeroDivisionError:
    print("Zero division occured")

except TypeError:
    print(" Handled unsupported operand type(s) for +: 'int' and 'str' ")



try:
    print(int("apple"))
    print(5+"apple")
except Exception as e:
    print(e)


class AgeLimit(Exception):
    pass 

def checkage(age):
    if age<18:
        raise AgeLimit("Below  18")
    else: 
        print("you are Eligible")

try :
    checkage(113)
except Exception as e: 
    print(e)



def checkage(age):
    if age<18:
            raise TypeError("Below  18")
    else: 
        print("you are Eligible")
    
try :
    checkage(11)
except Exception as e: 
    print(e)
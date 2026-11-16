 - process of creating,reading,writing ,update  and delete file using python


why we need file handling

- to store data permanently 
- to retrieve stored information
- update and delete 

types of file 

1. text file  (txt,.csv,.json,.xml)
2. binary file  (.jpg,.png,.pdf,.mp3,.mp4)  

Syntax: 

file =open("filename","mode") 
file.close()

mode: 
r => reading exsisting file 
w => write , creates or overwrite 
a => append the data at the end 
x => create a new file 
r+ => read and write 
w+ => write and read; overwrite 
a+ => append and read 

rb => read binary 
wb => write binary 
ab => append binary 

# write into file 

write() => single line 
writelines() => multiple string into file 

file =open("lega.txt","w")
file.write("Python Programming")
file.close()

file =open("lega.txt","w")
file.write("Welcome \n to skillfort")
file.close()


file =open("lega.txt","a")
file.write("\nHappy Learning")
file.close()


f=open("deepal.txt","w")
fruits=["Apple\n","Orange\n","Banana"]
f.writelines(fruits)
f.close()


# read  data from file  
read( )
readline()
readlines()


f=open("lega.txt","r")
print(f.read())
f.close()


f=open("lega.txt","r")
print(f.readline())
f.close() 

f=open("lega.txt","r")
data=f.readlines()
print(data[5])
f.close() 


# with 

with open("deepal.txt","r") as file :
    data=file.read()
    print(data)

# file pointer method
tell() - returns current position of the pointer
seek() - moves the file pointer to specific position 

with open("lega.txt","r") as f:
    print(f.tell())
    print(f.read(22))
    print(f.tell())
    print(f.readline())

f=open("sakthi.txt","x")  


import os 
if os.path.exists("sakthi1.txt"):
   print("Exists")
else:
   print("not found")

import os 
print(os.getcwd())
print(os.listdir())
print(os.path.exists("lega.txt")) 

data=b"Hello"
with open("sakthi.txt","wb") as f:
   f.write(data)


with open("rose.jpg","rb") as r:
   data=r.read()

with open("rose_arifa.jpg","wb") as t:
   t.write(data)
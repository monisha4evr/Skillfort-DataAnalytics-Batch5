import functools as f

lst=[1,2,3,4,5]
r=f.reduce(lambda a,c : a + c ,lst)
print(r)
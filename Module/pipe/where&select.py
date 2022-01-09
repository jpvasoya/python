from pipe import *
#where like filter
lst=[1,3,2,4,5]
x=list(lst|where(lambda x:x%2==0))
print(x)#[2,4]
#select like map
y=list(x|select(lambda x:x**x))
print(y)
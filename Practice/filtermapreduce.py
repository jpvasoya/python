from functools import reduce
lst=list(range(1,11))
print(lst)
x=list(filter(lambda a:a%2==0,lst))
print(x)
y=list(map(lambda a:a*2,x))
print(y)
z=reduce(lambda a,b:a+b,y)

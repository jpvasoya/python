#operations
import numpy as np
a=np.linspace(2,7,6,dtype=np.int16).reshape(2,3)
print(a)
b=np.array([(1,2,3),(4,5,6)])
print(b)
#a-b submition and addition
c=a-b
d=a+b
print(c)
print(d)
#b**2
e=b**3
print(e)
#condition apply return true false
f=e<35
print(f)

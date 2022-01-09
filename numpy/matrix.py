#matrix
from numpy import *
arr1=arange(0,18,2).reshape(3,3)
print(arr1)
arr2=ones(9,int).reshape(3,3)
print(arr2)
print(arr1+arr2)
arr3=arr1*arr2#simple multiply 2 array
print("simple multiply")
print()
print(arr3)
m1=matrix(arr1)
m2=matrix(arr2)
print("matrix multiply")
print(m1*m2)
#print(arr1.max())
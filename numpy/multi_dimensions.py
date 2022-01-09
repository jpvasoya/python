#multi dimensions array
from numpy import *
arr1=array([
[1,2,3],
[4,5,6],
[7,8,9]

])
print(arr1.ndim," dimensions array")
print(arr1)
arr2=arr1.reshape(3,3,1)
print(arr2.ndim,"dimensions array")
print(arr2)
print()
print("size of arr1:",size(arr1))
print("size of first row",len(arr1))

arr1[0][0]=9
arr1.sort()
print(arr1)
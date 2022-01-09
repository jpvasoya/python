from numpy import *
arr1=array(range(1,5))
print(arr1)
arr2=array(range(6,10))
print(arr2)
print(arr1+arr2)
print("sum of first array:",sum(arr1))
print(sqrt(arr1))#maths operations
print(concatenate([arr1,arr2]))#combined two array
print(sin(arr1))
print(max(arr1))
arr1[0]=9#update on a array1
print(arr1)
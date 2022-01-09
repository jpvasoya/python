#convert multi to one and single to multi
from numpy import *
#1.single to multi 
arr1=array([1,2,4,3,6,8,9,8,9,10,11,12])
print(arr1)
print()
print("2 dimensions")
print()
arr2=arr1.reshape(3,4)
print(arr2)
print()
print("3 dimensions")
print()
arr3=arr2.reshape(3,2,2)
print(arr3)
print()
#2.multi to single
arr=arr3.flatten()
print("3 to single dimensions")
print()
print(arr)

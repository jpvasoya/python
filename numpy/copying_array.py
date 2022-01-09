#copying array to another array
from numpy import *

print("1.assigning to copy")
print()
arr1=array(range(0,10,2))
print(arr1)
arr2=arr1#copy array but ......same address
print(arr2)
print(id(arr2),id(arr1))
#copying array no same address or different pointing objects
print("arr2 adress and arr1 adress")
print()
print("2.view method")
print()
arr2=arr1.view()
print(arr1,arr2)
print(id(arr2),id(arr1))
arr1[0]=5
#but in this one problem if we change value array that all other array value change
#dependent to both array
print(arr1,arr2)
#copying array without dependent and diff. address
print()
print("3.copy method")
print()
arr2=arr1.copy()
print(arr1,arr2)
print(id(arr1),id(arr2))
arr1[0]=9
print(arr1,arr2)

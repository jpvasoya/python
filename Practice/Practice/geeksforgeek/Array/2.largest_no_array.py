#find largest no in array
from array import *
lst=[1,2345,3,7,454,66,3,99,2]
arr=array('i',lst)
arr1=[]
for i in range(len(arr)):
	arr1.append(arr[i])
arr1.sort()	
print(arr1[len(arr1)-1])
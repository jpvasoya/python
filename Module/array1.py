from array import *
arr=array("i",[])
try:
	s_arr=int(input("enter length of the array:"))
	for i in range(s_arr):
		value=int(input("enter array value:"))
		arr.append(value)
	print(arr)
#search element on array
	search=int(input("search:"))
	for i in arr:
		if search==i:
			print("found at index of ",arr.index(search),	end=" ")
			break
	else:
		print("Not Found")
except ValueError:
	print("plz enter valid number")
	
	
	
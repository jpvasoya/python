#ways to find element is exist in list
lst=[1,2,3,4,5,6,7,9,10]
no=int(input("enter no:"))
#1. in operator
if no in lst:
	print("exist")
else:
	print("Not exist")
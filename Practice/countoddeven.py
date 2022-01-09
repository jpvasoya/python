def count(lst):
	print(lst)
	even,odd=0,0
	for i in lst:
		if int(i)%2==0:
			even+=1
		else:
			odd+=1
	return even,odd
	

lst=list(input("enter list:"))
even,odd=count(lst)
print(even)
print(odd)
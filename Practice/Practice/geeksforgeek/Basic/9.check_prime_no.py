# check prime no
no=int(input("enter no:"))
if no==0:
	print("it is Zero")
else:
	for i in range(2,no):
		if no%i==0:
			print("Not prime no")
			break
	else:
		print("prime no")
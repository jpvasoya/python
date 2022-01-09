#factorial number
try:
	no=int(input("enter a no which find fact:"))
	fact=1

	if no>=0:
		for i in range(1,no+1):
			fact*=i
		print(fact)
	else:
		print("enter a positive number")
except ValueError:
	print("Enter  Only Number")
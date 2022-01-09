#fibonacci series
no=int(input("enter no:"))
a,b=0,1
if no==1:
	print(a)
else:
	print(a)
	print(b)
	for i in range(2,no):
		c=a+b
		a=b
		b=c
		print(c)
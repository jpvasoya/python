def arm(n):
	sum=0
	temp=n
	order=len(str(n))
	while n>0:
		d=n%10
		sum=sum+d**order
		n=n//10
	if sum== temp:
		print("armstrong no")
	else:
		print("not armstrong no")
n=int(input("enter no:"))
arm(n)	
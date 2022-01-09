def fib(n):
	a=0
	b=1
	if n==0 or n<0:
		print("enter valid no")
	elif n==1:
		print(a)
	else:
		print(a)
		print(b)
		for i in range(2,n):
			c=a+b
			a=b
			b=c
			print(c)
		#print(c)
n=int(input("enter no:"))
fib(n)
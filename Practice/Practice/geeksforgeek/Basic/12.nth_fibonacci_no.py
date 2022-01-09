#nth multiple fibonacci no
def fib(n):
	if n<1:
		return 0
	elif n==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

no=int(input("enter no:"))
print(fib(no))

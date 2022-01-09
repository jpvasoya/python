def fact(n):
	if n==0:
		return 1
	return n*fact(n-1)
	
n=int(input("enter value:"))	
x=fact(n)
print(x)
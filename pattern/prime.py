def prime(n):
	if n%2==0 or n%3==0:
		print("its not prime no",n)
	else:
		print("it is prime no",n)
n=int(input("enter no:"))
prime(n)
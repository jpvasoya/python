#prime
def prime(n):
	if n==0:
		print("its zero")
	else:
		for i in range(2,n):
			if n%i==0:
				print("not prime no")
				break;
		else:
			  print("its prime no")
			




n=int(input("enter no:"))
prime(n)
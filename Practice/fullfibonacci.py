#fibonacci
def fib(n,f):
		a,b=0,1
		if n==1:
			print(a)
		elif n==0:
			print("enter valid no")
		else:
			print(a)
			print(b)
			lst=[0,1]
			for i in range(2,n):
				c=a+b
				a=b
				b=c
				lst.append(c)
				print(c)
			print(f"sum of {n} numbers fibbonacci is {sum(lst)}")
			count=0
		#print(lst)
			for i in lst:
				if i>=f:
					print(f"searched no is last in less {lst[count-1]}")
					break
				count+=1


try:			
	n=int(input("enter no :"))
	f=int(input("find no on fibbo:"))	
	fib(n,f)
except ValueError:
	print("Invalid Literals")
#factorial
from math import factorial as f
try:
	n=int(input("enter no:"))
	print(f(n))
except ValueError:
	print("Enter valid no")

def fact(n):
	if n>=0:
		f=1
		for i in range(1,n+1):
			f=f*i
		print(f)
	else:
		print("enter valid no")
try:
	fact(n)
except NameError:
	print("enter valid no")
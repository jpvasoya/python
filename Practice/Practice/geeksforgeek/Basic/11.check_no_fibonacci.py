#check fibonacci no or not
def fib(n):
	if n<=1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

n=int(input("enter no:"))
a,b=0,1
check=[a,b]
for i in range(1,n-1):
	x=fib(i)
	if x>n:
		break
	else:
		check.append(x)
if n in check:
	print("its fibonacci no")
	print(check)
else:
	print("not fib no")
	print(check)

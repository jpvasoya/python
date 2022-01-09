#compound interest
#monthly compounded
try:
	p=float(input("Enter deposite amount:"))
	r=float(input("enter rate(%):"))
	t=float(input("enter time period(year):"))
	n=12 #monthly compounded
	r=r/100
	nt=n*t
	amount=p*pow((1+r/n),nt)
	print(f'amount is {amount}')
except ValueError:
	print("invalid no")
	
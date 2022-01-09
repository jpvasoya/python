#simple interest
try:
	p=float(input("Enter principle amount:"))
	r=float(input("enter rate(%):"))
	t=float(input('enter time(year):'))
	r=r/100
	si = p*r*t
	print(f'simple interest is S.I. :{si}/-')
except ValueError:
	print("Invalid Number")
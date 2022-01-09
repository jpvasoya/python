import m
a=float(input('enter 1st value:'))
b=float(input('enter 2nd value:'))
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
n=int(input("select:"))
if n==1:
	m.add(a, b)
elif n==2:
	m.sub(a,b)
elif n==3:
	m.mul(a,b)
elif n==4:
	m.div(a,b)
else:
	print('invalid selection')
	
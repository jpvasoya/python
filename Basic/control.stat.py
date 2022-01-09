#control statement
mark=23
m=int(input('enter mark:'))
if m>=mark:
	print('you are passed')#if-else statement
else:
	print('better luck next time')


if m>80:
	print('A grade',m)
elif 70<m<=80:
	print('B grade',m)#ladder or if- elif statement
elif 23<=m<=70:
	print('C grade',m)
else:
	print('F grade',m)
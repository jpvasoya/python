def fun(a=5,b=None,c=None):
	if b==None and c==None:
		sum=a
	elif c==None:
		sum=a+b
	else:
		sum=a+b+c
	return sum
print(fun(6))

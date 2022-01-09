#variable length arguments
def var(arg1,*vart):
	print(arg1)
	for n in vart:
		print(n)
	return
var(10)
var(10,20,30)#more than one arguments 
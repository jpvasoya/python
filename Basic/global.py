a=5
b=10
def scopev():
	#a=15
	x=globals()["b"]
	globals()["b"]=25
	print(b)
	print(x)
	global a
	a=3
	a=7
	print("in inside fun",a," ",id(a))
scopev()
print("outside fun",a, " " ,id(a))
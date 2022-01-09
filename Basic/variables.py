#variables or identifier
a=10
print(a)
a=10.0#float
print(a)
a='jp vasoya'
print(a)#string
a=0
print(bool(a))#boolean
#scope of variable

print("------------------------------------")
print("scope of variables")
x=21
def l():
	x=5#x=5 and y= 19 local variable
	y=19
	print(x)
l()
print(x)#x=21 global variable
print(y)#not access out of the function
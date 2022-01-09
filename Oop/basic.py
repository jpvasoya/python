class basic:
	"its simple oop program to show the maths operation"
	def add(x,y):
		add=print(x+y)
		return add
	def mul(x,y):
		mul=print(x*y)
		return mul
	def div(x,y):
		div=print(x/y)
		return div
	def sub(x,y):
		sub=print(x-y)
		return sub
	def __init__(self):
		x=int(input("enter 1st value:"))
		y=int(input("enter 2nd value:"))
		print(basic.add(x,y))
		print(basic.mul(x,y))
		print(basic.div(x,y))
		print(basic.sub(x,y))
#basic.add()
basic()
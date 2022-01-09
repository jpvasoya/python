class computer:
	var1=50
	def __init__(self,x):
		print("i am constructor i am automatically perform ")
		self.name=x
		print(x)
	def method(self,name):
		self.sname=name
		print(self.sname)


com1=computer("jaydip")
com1.method("vasoya")
computer.method(com1,"hello")
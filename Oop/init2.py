class computer:
	def __init__(self,name,price):
		self.nm=name
		self.pr=price
		
	def config(self):
		print("Computer:::--",self.nm," price is",self.pr)

com1=computer("Dell","25000")
com1.config()	
com2=computer("Lenovo",100000)
com2.config()
#computer.config(com1,"Apple","100000")
#com2.config()

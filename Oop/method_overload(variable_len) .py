class method_o:
	def method(self,*data):
		self.sum1=sum(data)
		print(self.sum1)


m1=method_o()
m1.method(4,5,5,6)
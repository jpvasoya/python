class students:
	def __init__(self,name,rno):
		self.name=name
		self.rollno=rno
		self.lap=self.computer()#define object of the inner class
	def show(self):
		print(self.name+"  "+str(self.rollno))
		self.lap.show()
		
	#	self.s2=self.show()
		#print(self.s2)
	class computer:
		def __init__(self):
			self.brand="Dell"
			self.os="windows"
			self.price="30000"
		def show(self):
			print(self.brand,self.os,self.price)
s1=students("jay vasoya",51)
s1.show()
print(s1.lap.brand)
s1.lap.show()
com=students.computer()#outside of the define inner class' obj'
print(com.price)

		
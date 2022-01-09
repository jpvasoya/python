class series:
	def __init__(self):
		pass
	def fib(self,num):
		self.num=num
		self.a,self.b=0,1
		print(self.a)
		print(self.b)
		for i in range(2,self.num):
			self.c=self.a+self.b
			self.a=self.b
			self.b=self.c
			print(self.c)
	def fact(self,num):
		self.num=num
		self.fact=1
		for i in range(1,self.num+1):
			self.fact=self.fact*i
		print(self.fact)
			
s1=series()
num=int(input("enter no:"))
print("fibonacci:")
s1.fib(num)
print("factorials:")
s1.fact(num)

class method:
	def method(self,a=None,b=None,c=None):
		sum=0
		if a!=None and b!=None and c!=None:
			sum=a+b+c
		elif a!=None and b!=None:
			sum=a+b
		else:
			sum=a
		return sum
		

m1=method()
x=m1.method(1,3,5)
print(x)
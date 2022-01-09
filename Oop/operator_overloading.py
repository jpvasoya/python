#operator overloading
class add:
	def __init__(self,m1,m2):
		self.m1=m1
		self.m2=m2
	def __mul__(self,other):
		m1=self.m1*other.m1
		return m1


s1=add(10,56)
s2=add(34,40)
s3=s1*s2
print(s3)
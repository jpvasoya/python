class students:
	school="J.j.kundaliya"
	def __init__(self,m1,m2,m3):
		self.m1=m1
		self.m2=m2
		self.m3=m3
	def avg(self):
		return (self.m1+self.m2+self.m3)/3
	def get_m1(self):#get method
		return self.m1
	def set_m1(self,m1):#set method
		self.m1=m1
	@classmethod
	def info(cls):
		return cls.school
	@staticmethod
	def static():
		print("static method")
	
s1=students(100,92,83)
print("avg marks:")
print(str(s1.avg())+"%")
print("before set method m1 value")
print(s1.get_m1())
s1.set_m1(50)
print("after set method value of m1:")
print(s1.m1)
print(students.info())
s1.static()
		
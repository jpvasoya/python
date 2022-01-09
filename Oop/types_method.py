#types of method
class method:
	gender="male"
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def method(self):  #instance method
		print(self.name)
	@classmethod
	def class_method(cls):#class method call to class and instances
		print(cls.gender)
	@staticmethod
	def info():
		print("this is static method")
		
		
m1=method("jay","vasoya")
y=m1.method()
m1.class_method()
m2=method("jp","vasoya")
x=m2.method()
method.class_method()
method.info()
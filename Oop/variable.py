class car:
	wheels=4#class variabl3
	def __init__(self):
		self.name="BMW"#instnce variable
		self.model="CDI"
c1=car()
c2=car()
print(c1.name,c1.model,c1.wheels)
c2.name="Mercedese"#instance variable
c1.wheels=5

print(c2.name,c2.model,c2.wheels,c1.name)
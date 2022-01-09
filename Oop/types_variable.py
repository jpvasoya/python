#types of variable
class variable:
	gender="male"
	def __init__(self):
		self.name="jay vasoya"#instance variable
		self.age=18
	def view(self):
		print(self.name,self.age)


var=variable()
var.age=21
var.view()
variable.gender="female"
print(var.gender)
newVar=variable()
print(newVar.gender)
newVar.view()
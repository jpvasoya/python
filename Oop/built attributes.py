#class attributes
class jp:
	'hello my name is Jay also called me jp'
	def __init__(self, name):
		self.name=name
	def dis(self):
		print(self.name)
t=jp(name=input('enter name:'))
t.dis()
print(jp.__doc__)#documention string 
print(jp.__class__)#type
print(jp.__name__)#name of the class
print(jp.__bases__)
print('module:',jp.__module__)
print('\n')
print(jp.__dict__)

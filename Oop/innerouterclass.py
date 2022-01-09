class outer:
	def __init__(self):
		print("its work!! outer class")
		self.obj=self.inner()
	def show(self):
		pass
	class inner:
		def __init__(self):
			print("its work!! inner class")
		def show(self):
			pass


obj=outer()
obj1=outer.inner()
obj2=obj.inner()
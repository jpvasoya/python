#method overiding
class a:
	def method(self,a,b):
		print("hii i am working")
	def method(self):
		print("im")
	def method(self):
		print("all is above huhhhh")


class b(a):
	def method(self,a):
		print("im in b")
		super().method()


a1=b()
a1.method(7)
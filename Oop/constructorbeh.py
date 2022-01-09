#constructor 
class A:
	def __init__(self):
		print("its working in A")
	def feature1(self):
		print("feature 1 working")
class B(A):
	if False:
		def __init__(self):
			print("its working in B")
	def feature2(self):
		print("feature 2 working")

#a=A()
b=B()
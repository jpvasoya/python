#super ,Method Resolution Order
class A:
	def __init__(self):
		print("its working in A")
	def feature1(self):
		print("feature 1 working in A")
class B:
	def __init__(self):
		print("its working in B")
	def feature1(self):
		print("its working feature 1 in B")

class C(B,A):
	def __init__(self):
		super().feature1()
	

	
b=C()
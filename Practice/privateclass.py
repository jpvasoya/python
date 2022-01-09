class test:
	__try1="hello"
	def __init__(self):
		print("its work")
	def __method(self):
		print(self.__try1)
	
	
t=test()
print(t._test__try1)
t._test__method()
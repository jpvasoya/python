class computer:
	def __init__(self):
		print("its automatically call when object creation of the class")
	def config(self):
		print("its config file in computer class")

com1=computer()	
#computer.cofig(com1)
com1.config()
com2=computer()
print("-------------------------------------")
for i in range(5):
	com3=computer()
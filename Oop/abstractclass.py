#abstract class
from abc import ABC,abstractmethod

class comp(ABC):
	@abstractmethod
	def compulsory(self):
		print("hello")

class a(comp):
	def compulsory(self):
		print("hii")
		super().compulsory()

a1=a()
a1.compulsory()
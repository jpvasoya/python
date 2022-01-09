#palindrome num
class palindrome:
	def __init__(self):
		self.no=input("enter no:")
	def pldmno(self):
		self.r_no=self.no[::-1]
		if self.no==self.r_no:
			print("its palindrome no")
		else:
			print("not a palindrome no")
		

#p1=palindrome()
#p1.pldmno()
class try1(palindrome):
	pass


#p2=palindrome()
#p2.pldmno()
	
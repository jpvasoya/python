#python constructor
class student:
	count=0
	def __init__(s, name, id,address):
		s.name=name
		s.id=id
		s.address=address
	def show(s):
		print("------------------------------------")
		print(s.name)
		print(s.id)
		print(s.address)
		print("------------------------------------")
t=student(name=input('enter stud. name:'), id=int(input('enter id:')), address=input('enter city:')) 
t.show()

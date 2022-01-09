phone=input("enter no:")
dict={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",
6:"Six",7:"Seven",8:"Eight",9:"Nine",0:"Zero"}
try:
	for i in phone:
			print(dict.get(int(i),"Not found "),end=" ")
except ValueError:
	print("invalid value")
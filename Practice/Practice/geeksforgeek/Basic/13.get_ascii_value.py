#ascii value of the character
try:
	char=input("enter character:")
	print(ord(char))
except Exception as e:
	print("---------------------------------------------------")
	print(e)
	print("---------------------------------------------------")

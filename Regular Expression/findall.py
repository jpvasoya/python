#find all
import re
ex="@gmail.com"
inpt=input("enter email:")
if re.findall(ex,inpt):
	print("valid email")
else:
	print("not valid email")
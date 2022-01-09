#reg exp
import re
ex="@gmail.com"
ptn=input("enter email:")
if re.match(ex,ptn):
	print("Valid email")
else:
	print("not valid email")
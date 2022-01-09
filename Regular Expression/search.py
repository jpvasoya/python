#search
import re
ex="@gmail.com"
pattern="jpvasoya@gmail.com"
ptn=input("enter email:")
if re.search(ex,ptn):
	print("valid email")
else:
	print("not valid email")
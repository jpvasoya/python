#match method
import re
ex="@gmail.com"
ptn=input("enter email:")
match=re.match(ex,ptn)
if match:
		print("valid email")
		print(match.group())
		print(match.start())
		print(match.end())
		print(match.span())
else:
		print("not valid email")
		#print(match.start())
inpt=input("enter phrase:")
text=inpt.split()
a=''
for i in text:
	a+=i[0].upper()
print(a)
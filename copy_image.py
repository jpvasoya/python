f=open("sample.jpeg","rb")
f1=open("copy.jpeg","wb")
for i in f:
	f1.write(i)

#file position
data=open('jp.txt')
t=data.read(14)
print(t)
print("current position of cursor:",data.tell())
#tell()method give position of the cursor
data.seek(0)#seek()method using to moved to cursor
print("current position of cursor:",data.tell())
t1=data.read()
print(t1)
data. close()
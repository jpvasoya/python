#reading data
data=open('jp.txt','r')
t=data.read(14)#14 bytes data access
print(t)
print("------------------------------------")
t1=data.read()#full data access
print(t1)
data.close()
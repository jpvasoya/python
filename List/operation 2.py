#operation 2
#1.updation
l=[1, 'hello',2,3,4,"jay","vasoya"]
l[1]='welcome'
print(l)
#2.insertion
print (l.append('hello'))
print(l)
l.append('🤨🧐')
print(l)
#l. append('h1','h2')not allowed literal not allowed
l.append(['h1',"h2"])
print(l)
#deletion
del(l[9])
print(l)
del(l[8])
del(l[7])
print(l)
del(l)#whole list delete
print(l)
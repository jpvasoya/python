#method 3
#1.pop(index)
l=[1, 'hello',2,3,4,"jay","vasoya"]
l. pop()#last obj removed
print(l)
l. pop(1)#specific obj remove d
print(l)
#l. pop('hello')obj not allowed as argument
#2.remove
l. remove(1)#argument as a obj
print(l)
l. remove('jay')
print(l)
del(l[0])#function
print (l)
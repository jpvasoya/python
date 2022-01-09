#operation of the tuples
#1.adding
t1=(2,99,3,1,'jay')
t2=('jp','vasoya')
t3=t1+t2
print(t3+('hello',))#it's valid
#2.replicating
print(2*t2)
#update not allowed
#t1[0]=5
#print(t1)
#3.deletion
del(t1)#whole tuples delete
print(t1)
#del(t2[1])#tuples in specific obj not allowed to delete

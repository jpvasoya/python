#method 1
#1.copy()
d1={1:'jp', 'king':'vasoya',3:'where', 4:'are'}
d2=d1.copy()
print(d2)#copy to another dictionary
print(d1)
#2.clear()
d1.clear()#clear all entries
print(d1)
#3.update()
d1={1:'jay', 2:'jp'}
d2.update(d1)
print(d2)
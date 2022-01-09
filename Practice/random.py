import random as r
def dice():
	#roll=(1,2,3,4,5,6)
	result1=r.randint(1,6)
	result2=r.randint(1,6)
	return (result1,result2)
print(dice())
	
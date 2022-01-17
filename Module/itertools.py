import itertools as it

#1.count function
counter=it.count(start=2,step=2)
#for i in counter:
#	print(i)
#	if i==100:
#		break
data=[100,300,400,500]
#col=list(zip(counter,data))
#print(col)

#2.zip_longest function
#col=list(it.zip_longest(range(10),data))
#for count in counter:

#	#3. cycle function
#	data=it.cycle(data)
#	print(next(data))
#	if count==100:
#		break
#print(next(data))

#4.repeat function
repeat=it.repeat(data,times=3)
for count in counter:
	print(next(repeat))
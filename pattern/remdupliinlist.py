#remove duplicates in the list
List=[5,4,3,2,99,2,1,2,1,99,40,52,2]
Unique=[]
for i in List:
	if i in Unique:
		pass#continue
	else:
		Unique.append(i)
		
print(Unique)


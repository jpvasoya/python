List=[12,90,2,9,2,89,22,33,6,6,1]
max=List[0]
print("maximum number of the list")
for i in List:
	if max<i:
		max=i
print(max)
print("minimum number of the list")
for i in List:
	if max>i:
		max=i
else:
	print(max)
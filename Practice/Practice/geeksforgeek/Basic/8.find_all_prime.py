no=int(input("enter no:"))
for i in range(2,no):
	for j in range(2,i):
		if i%j==0:
			break
	else:
		print(i)
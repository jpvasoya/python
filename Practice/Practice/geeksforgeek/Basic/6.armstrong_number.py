#armstrong no
no=input("no:")
d=len(no)
#print(d)
sum=0
for i in no:
	sum+=pow(int(i),int(d))

no=int(no)
if sum==no:
	print("Armstrong Number")
else:
	print("Not a armstrong number")
	

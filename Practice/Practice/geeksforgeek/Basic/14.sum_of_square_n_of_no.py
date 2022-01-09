#sum of natural no square
no=int(input("enter no:"))
no=abs(no)
sum=0
for i in range(no+1):
	sum+=i*i

print(sum)
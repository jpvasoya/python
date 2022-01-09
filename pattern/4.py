def pattern(n):
	for i in range(n):
		for j in range(n-i):
			print("*",end=" ")
		print("\n")
	for i in range(n):
		if i==0:
			continue
		for j in range(i+1):
			print("*",end=" ")
		print("\n")
n=int(input("enter no:"))
pattern(n)

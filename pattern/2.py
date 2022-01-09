def pattern(n):
	for i in range(n):
		for j in range(n-i):
			print("*",end=" ")
		print("\n")
n=int(input("enter no:"))
pattern(n)

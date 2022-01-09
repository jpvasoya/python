#num pattern
print("\nfirst pattern row wise\n")

def pattern(n):
	for i in range(0,n):
		for j in range(i+1):
			print(i+1,end=" ")
		print()
pattern(5)
print("\nsecond pattern collumn wise\n")
def pattern2(n):
	for i in range(0,n):
		for j in range(i+1):
			print(j+1,end=" ")
		print()
pattern2(5)
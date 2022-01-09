#linear search using function and keyword
lst=[1,5,8,23,67,34,54,4,5]
n=int(input("enter no:"))
if n in lst:
	print("found at {}".format(lst.index(n)))
else:
	print("Not found")
#using own logic	
def search(n):
	for j in range(len(lst)):
		if n==lst[j]:
			print(f"found at {j}")
			break
	else:
		print("not found")

search(n)			
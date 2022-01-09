#binary search
lst=[4,5,6,23,4,79,67,34,89]
lst.sort()
print(lst)
n=int(input("enter a number:"))
def search(n):
	l=0
	u=len(lst)
	while l<=u:
		mid=l+u//2
		if lst[mid]==n:
			print(f"found at {lst.index(n)}")
			break
		else:
			if lst[mid]<n:
				l=mid
			else:
				u=mid
	
	else:
		print("not found")

search(n)
				
	
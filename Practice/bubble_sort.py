#bubble sort
def sort(lst):
	for i in range(len(lst)-1,0,-1):
		for j in range(i):
			if lst[j]>lst[j+1]:
				lst[j],lst[j+1]=lst[j+1],lst[j]



lst=[5,4,8,7,2]
sort(lst)
print(lst)
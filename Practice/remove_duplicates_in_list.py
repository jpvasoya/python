lst=[1,2,3,2,5,3,5,3,4,6]
#remove duplicate 
lst1=list(set(lst))
print(f"before the list :\n{lst}\nafter remove duplicates list:\n{lst1}")
#duplicate value 
new_lst=[]
dup_lst=[]
for i in lst:
	if i not in new_lst:
		new_lst.append(i)
	else:
		dup_lst.append(i)

print(f"remove duplicate list:\n{new_lst}")
print(f"duplicate list item:\n{dup_lst}")
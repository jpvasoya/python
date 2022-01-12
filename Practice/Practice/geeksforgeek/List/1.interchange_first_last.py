#interchange first and last element
lst=[9,1,2,3,4,5,6,7,8,0]
#print(dir(lst))
#lst.sort()
#print(lst)
lst[0],lst[len(lst)-1]=lst[len(lst)-1],lst[0]
print(lst)
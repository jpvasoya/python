#swap 2 elements 
lst=[1,2,3,4,5,6,7,8,9,0]
print("choose:")
print("1.swap by index")
print("2.swap by value")
choose=int(input("Enter 1or 2:"))
no1=int(input("enter 1st no:"))
no2=int(input("enter 2nd no:"))
def swap_by_value(no1,no2):
	#find index
	ind1=lst.index(no1)
	ind2=lst.index(no2)
	lst[ind1],lst[ind2]=lst[ind2],lst[ind1]
	print(lst)

def swap_by_index(no1,no2):
	lst[no1],lst[no2]=lst[no2],lst[no1]
	print(lst)
if choose==1:
	print("swap before list:")
	print(lst)
	print("swap after list")
	swap_by_index(no1,no2)
else:
	print("swap before list:")
	print(lst)
	print("swap after list")
	swap_by_value(no1,no2)


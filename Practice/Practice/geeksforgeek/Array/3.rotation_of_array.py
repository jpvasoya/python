import array
arr=array.array("i",[1,2,43,4,5,6,7])
no=int(input("where to rotate:"))
if no<=len(arr):
	print(f"rotation before array:\n{arr}")
	arr_len=len(arr)
	temp=[]
	for i in range(arr_len):
		if i<no:
			temp.append(arr[i])
	arr.extend(temp)
	del arr[0:no]
	print(f"rotation after array:\n{arr}")
else:
	print("enter valid range")	
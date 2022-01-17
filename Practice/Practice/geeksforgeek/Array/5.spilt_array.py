arr=[1,2,33,4,5,6,7]
no=int(input("enter no to split:"))
if no in arr:
	new_arr=[]
	for i in arr:
		new_arr.append(i)
		last_index=arr.index(i)
		if i==no:
			break
	del arr[0:last_index+1]
	arr.extend(new_arr)
	print(arr)
else:
	print("Enter valid value")
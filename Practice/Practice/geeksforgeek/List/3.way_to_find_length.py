#way to find length of list
from operator import length_hint
lst=[1,2,3,4,5,6,7,8,9]
#1.len function
print(f"length of list:{len(lst)}")
print(lst.__len__())

#2.using iteration
len=0
for i in lst:
	len+=1
print(f"length of list using iterations:{len}")

#3.using length_hint function
print(f"using length_hint:{length_hint(lst)}")
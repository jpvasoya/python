#pre def function 4
#1.count(sub string,beg, end) 
s='Jay vasoy'
print("\n1.count")
print (s.count('a'))
print(s.count('a',2,5))#counting 
print(s.count('Jay'))
#2.index(same as count)
print('\n2.index')
print (s.index('a'))#find index 
print(s.index('a',2,6))#if not in range error                                         generate
#3.find(same as index)
print('\n3.find')
print(s.find('a'))#find index 
#if not in range give another index
print (s.find('a',2,5))
print (s[-1])
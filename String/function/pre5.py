#pre df function 5
#1.strip(sub string), lstrip(), rstrip()
print('\n1.strip')
s='jp vasoya jp'
print (s.strip('jp'))#remove both sides
print (s.lstrip('jp'))#remove left side
print (s.rstrip('jp'))#remove right side
#2.replace(old substring, new substring ,how manytime)
s='jp jp jp jay'
print('\n2.replace')
print(s.replace('jp','jay'))
print(s.replace('jp','jay',1))
#3.split()
print("\n3.split")
print (s.split(' '))#space to splitting
s="my@name@is@jay@@@@@"
print(s.split("@",3))#how many times
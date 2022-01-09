#function arguments
#1.position argument
print("position argument")
def pos(name,age):
	print(name,end=" ")
	print(age)
pos("jp",21)
print()
print("defualt argument")
#2.keyword argument
def keyword(name,age):
	print(name,end=" ")
	print(age)
keyword(28,"jp")
keyword("jp",age=28)
keyword(age=28,name="jay")
print()
#3.defualt argument
print("defualt argument")
def defualt(name,age=18):
	print(name,end=" ")
	print(age)
defualt("jaydip")
print()
#4.variables length argument
print("variables length argument")
def varlen(a,*b):
	print(a)
	print(b)
	c=a+sum(b)
	print(c)
varlen(2,6,7,8,9,10)
print()
#5.keyworded variables length argument
print("keyword length argument")
def kwargs(a,**b):
	print(a)
	print(b)
kwargs("jp",sname="vasoya",age=21,fname="pravinbhai")
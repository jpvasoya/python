#keyword variable length argument
#**kwargs
def fun(*data):#variable length argument
	print(data)
fun("jp","vasoya")
def fun1(**data):
	print(data)
#	print(data.items())
fun1(name="jp",sname="Vasoya")



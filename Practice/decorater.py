#decorators
def sub(a,b):
	print(a-b)


def subfeture(func):
	def main(x,y):
		if x<y:
			x,y=y,x
		return func(x,y)
	return main
sub=subfeture(sub)
if __name__=="__main__":
	sub(1,5)




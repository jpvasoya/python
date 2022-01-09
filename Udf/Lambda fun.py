#lambda function or anonymous
#normal fun
def sqr(x):
	s=x*x
	return(s)
#anonymous fun
square=lambda x:x*x
#calling normal fun
print("sqr:",sqr(2))
#calling lambda fun
print("sqr=",square(2))
#simple interest
amount=0
rate=0
time=0
def si(amount,time,rate):
	si= (amount*time*rate)/100
	return print(si)
a=int(input("enter principle amounts:"))
t=int(input("enter time of the interest:"))
r=int(input("enter rate of the interest:"))
si(a,t,r)
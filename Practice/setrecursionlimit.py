import sys
n=5
def call():
	print(sys.getrecursionlimit())
	for i in range(10):
		if i==5:
			call()
			break
		else:
			print("stop")
sys.setrecursionlimit(100)
call()
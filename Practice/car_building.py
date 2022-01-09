help="""
	 -start command to start a car
	 -stop command to stop a car
	 -quite or exit to close 
 'help to define all'
	  """
started=False
while True:
	user=input(">").lower()
	if user=="help":
		print(help)
	elif user=="start":
		if started:
			print("car is already started")
		else:
			started=True
			print("car is start")
	elif user=="stop":
		if started:
			print("car is stop")
			started=False
		else:
			print("car is already stop")
	elif user=='exit' or user=='quite':
		break
	else:
		print(f"No command found {user}, Please type 'help'")
else:
	print("thank for visit")
	


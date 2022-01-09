#area of the circle
π=22/7
try:
	r=int(input('Enter a r:'))
	area=(π*r*r)/2
	print(f"area of circle is {area}")
except ValueError:
	print("Enter a valid number")
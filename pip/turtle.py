import turtle as t
a=0
b=0
t.bgcolor("#000000")
t.speed(0)
t.pencolor("red")
t.penup()
t.goto(0,200)
t.pendown()

while True:
	t.forward(a)
	t.right(b)
	a+=3
	b+=1
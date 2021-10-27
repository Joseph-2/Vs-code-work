import turtle as turt
turt.speed(0)
def move(xx,yy):
  turt.penup()
  turt.goto(xx,yy)
  turt.pendown()

def petal(color):
  turt.fillcolor(color)
  turt.begin_fill()
  turt.circle(70,90)
  turt.left(90)
  turt.circle(70,90)
  turt.end_fill()

move(0,-100)
move(-400,-400)
turt.fillcolor("sky blue")
turt.begin_fill()
for x in range(4):
  turt.forward(800),turt.left(90)
turt.end_fill()
move(0,0)
turt.pensize(30)
turt.pencolor("lime green")
turt.goto(0,-400)
turt.pensize(1)
turt.pencolor("black")
turt.fillcolor("brown")
move(0,-100)
turt.begin_fill()
turt.circle(100)
turt.end_fill()
move(0,-80)
for x in range(25):
  turt.right(135)
  petal("gold")
  turt.right(135)
  turt.penup()
  turt.circle(80,15)
  turt.pendown()
move(15,-275)
turt.pencolor("lime green")
petal("lime green")
turt.pencolor("white")
move(-400,200)
turt.left(75)
for x in range(4):
  turt.fillcolor("white")
  turt.begin_fill()
  turt.circle(50)
  turt.end_fill()
  turt.penup()
  turt.forward(50)
  turt.pendown()



wn = turt.Screen()
wn.mainloop()
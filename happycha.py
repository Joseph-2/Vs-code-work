#members: Hasan Ahmad, Souichioru Kotaki, Andrew Chung, Joseph Moyles
import turtle as t
t.speed(0)

#functions
def move(xx,yy):
    t.penup(),t.goto(xx,yy),t.pendown()

def hash_marks_x():
    t.penup()
    t.goto(-200, 0)
    for i in range(40):
        t.lt(90)
        t.pendown()
        t.fd(5)
        t.color("light grey")
        t.fd(195)
        t.bk(195)
        t.color("black")

        t.bk(10)
        t.color("light grey")
        t.bk(195)
        t.fd(195)
        t.color("black")
        t.fd(5)
        
        t.penup()
        t.rt(90)
        t.fd(10)

def hash_marks_y():
    t.penup()
    t.goto(0, 200)
    for i in range(40):
        t.pendown()
        t.fd(5)
        t.color("light grey")
        t.fd(195)
        t.bk(195)
        t.color("black")

        t.bk(10)
        t.color("light grey")
        t.bk(195)
        t.fd(195)
        t.color("black")
        t.fd(5)
        
        t.penup()
        t.rt(90)
        t.fd(10)
        t.lt(90)

#hash marks
hash_marks_x()
hash_marks_y()

#x+y axis
move(-200,0)
t.forward(400)
move(0,0)
t.left(90)
t.forward(200)
t.backward(400)
move(-200,-200)

# box coordinate plane
for i in range(4):
    t.forward(400)
    t.right(90)
    
#equation line and stamping (arrows)
equation = input("Please enter an equation in y = mx + b format: ")
'''
slope = int(equation[4])
yint = int(equation[9])
'''
equation = equation.split("x")
slope = int(equation[2])
yint = int(equation[6])


move(0,yint)
angle = 90 - 45/slope
t.setheading(angle)
t.color("red")
t.forward(200)
t.stamp()
t.backward(400)
t.right(180)
t.stamp()


# finish
wn = t.Screen()
wn.mainloop()
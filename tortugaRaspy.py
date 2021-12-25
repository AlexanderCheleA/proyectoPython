import turtle
import time
from random import randint

s=turtle.Screen()
t=turtle.Turtle()
s.bgcolor('gray') #Establece el color de la pantalla con color gris

time.sleep(0) #0 para q valla rapido 1 despacio 10 rapido                    
t.penup()
t.goto(-140,140)

for paso in range(15):
    t.write(paso, align='center')
    t.right(90)
    t.forward(10)
    t.pendown()
    for lineaAlzada in range(15):
        t.forward(10)
        if lineaAlzada % 2==0:
            t.penup()
        else:
            t.pendown()
    #t.forward(150)
    t.penup()
    t.backward(160)
    t.left(90)
    t.forward(20)

t.color('red')
t.shape('turtle')
t.penup()
t.goto(-160,100)
for turn in range(36):
    t.right(10)
t.pendown()

b=turtle.Turtle()
b.color('blue')
b.shape('turtle')
b.penup()
b.goto(-160,70)
for turn in range(72):
    b.left(5)
b.pendown()

o=turtle.Turtle()
o.color('orange')
o.shape('turtle')
o.penup()
o.goto(-160,40)
for turn in range(36):
    o.right(10)
o.pendown()

p=turtle.Turtle()
p.color('purple')
p.shape('turtle')
p.penup()
p.goto(-160,10)
for turn in range(72):
    p.left(5)
p.pendown()

for turno in range(100):
    t.forward(randint(1,5))
    b.forward(randint(1,5))
    o.forward(randint(1,5))
    p.forward(randint(1,5))


#p.forward(20*15)

turtle.done()

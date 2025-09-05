from turtle import right, left, forward, backward, speed
import room

speed(100)

window = room.draw_room(level = 4, n_alcoves = 1, radius = 5)

###
# Start your code here
x = 40
for i in range(3):
    forward(x)
    right(90)
    forward(3*x)
    left(90)
    forward(x)
    right(90)
    forward(x)
    left(90)
    forward(3*x)
    right(90)
    forward(x)
    left(180)

forward(x)
right(90)
forward(3*x)
left(90)
forward(x)
right(90)
forward(x)
left(90)
forward(6*x)
left(90)
forward(7*x)
left(90)
forward(6*x)
left(90)
forward(6*x)
left(90)
forward(5*x)
left(90)
forward(5*x)
left(90)
forward(4*x)
left(90)
forward(4*x)
left(90)
forward(3*x)
left(90)
forward(3*x)
left(90)
forward(2*x)
left(90)
forward(2*x)
left(90)
forward(x)
left(90)
forward(x)
left(90)
forward(9*x)
for i in range(4):
    left(180)
    forward(x)
    left(90)
    forward(x)
    right(90)
    forward(x)
    left(90)
    forward(x)

# End your code here
###
 
window.exitonclick()
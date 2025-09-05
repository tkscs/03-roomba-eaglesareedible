from turtle import right, left, forward, backward, speed
import room


n_alcoves = 3


# Draw the Level 5 version of the room
window = room.draw_room(level = 5, n_alcoves = n_alcoves)

###
# Start your code here
speed(100)

x = 40

for i in range(4):
    forward(x)
    left(90)
    forward(x)
    right(90)
    forward(x)
    left(90)
    forward(x)
    left(180)

forward(5*x)
right(90)
forward(3*x)
left(90)
forward(x)
right(90)
forward(x)
left(90)
forward(3*x)
right(90)
forward(5*x)
left(180)

for i in range(4):
    forward(x)
    left(90)
    forward(x)
    right(90)
    forward(x)
    left(90)
    forward(x)
    left(180)

forward(5*x)
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
forward(3*x)
right(90)
forward(5*x)
left(180)
for i in range(4):
    forward(x)
    left(90)
    forward(x)
    right(90)
    forward(x)
    left(90)
    forward(x)
    left(180)
forward(5*x)
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

 
# End your code here
###
 
window.exitonclick()
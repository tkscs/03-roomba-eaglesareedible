# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author:
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code hered
for i in range(3):
    forward(150)
    left(90)
    forward(40)
    left(90)
    forward(150)
    right(90)
    forward(40)
    right(90)
# End your code here
###
 
window.exitonclick()
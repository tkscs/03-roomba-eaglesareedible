# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import left, forward, backward
import room

# Draw the Level 1 version of the room
window = room.draw_room(level = 1)

###
# Start your code here
for i in range(3):
    forward(150)
    left(90)
    forward(40)
    left(90)
    forward(150)
    left(270)
    forward(40)
    left(270)
 
 
# End your code here
###
 
window.exitonclick()
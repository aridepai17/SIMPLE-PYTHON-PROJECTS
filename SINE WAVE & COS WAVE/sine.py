from turtle import *
from math import *

A = 50 #Amplitude
B = 100 #Wavelength
C = 0 #Horiziontal offset
D = 0 #Vertical offset

penup()

for x in range(-200, 200):
    #Sine Wave function
    y = A * sin((2 * pi / B) * ( x + C)) + D
    goto(x, y)
    pendown()
    
hideturtle()
mainloop()
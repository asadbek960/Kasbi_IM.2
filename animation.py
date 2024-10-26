from turtle import *
import colorsys as colorsys
bgcolor("black")
speed(0)
tracer(5)
hideturtle()
hue=0.0
for i in range(500):
    col=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(col)
    fd(i)
    lt(144)
    hue+=1/720
done()
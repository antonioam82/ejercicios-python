from tkinter import *
import math
from itertools import cycle, islice

ee = 0.05
_OuterDia = 300
_width = 800
_height = 600
_vertices = 6

def get_coords(od,cx,cy,vertices=3,offset=0):
    angle = 2*math.pi/vertices
    return [[math.cos((angle*i)+(offset*math.pi/180))*od/2+cx,
             math.sin((angle*i)+(offset*math.pi/180))*od/2+cy]for i in
            range(0,vertices)]

def spiral_viral(points,color,_range):
    points.append(points[0])
    for i in range(0,_range):
        r = [draw(j,points,color[j%_vertices])for j in range(0,len(points)-1)]
        points = [[ee*points[i][0]+(1-ee)*points[i+1][0],ee*points[i][1]+
                   (1-ee)*points[i+1][1]]for i in range(0,len(points)-1)]
        points.append(points[0])
        color.append(color.pop(0))

draw = lambda i,p,c : canvas.create_line(p[i][0],p[i][1],p[i+1]
                                         [0],p[i+1][1],fill=c)

root = Tk()
root.title("POLI")
canvas = Canvas(width=_width,height=_height,bg='black')

color = ['yellow','white','red','pink','green','light blue']
pt = get_coords(_OuterDia,_width/2,_height/2,_vertices,0)
spiral_viral(pt,color,50)

canvas.pack()
mainloop()

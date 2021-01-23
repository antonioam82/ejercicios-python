import tkinter as tk
from random import randint,uniform,random
import math

SCALE = 255
NUM_CIVS = 15600000

root = tk.Tk()
root.title("Milky Way Galaxy")
c = tk.Canvas(root,width=1000,height=800,bg="black")
c.grid()
c.configure(scrollregion=(-500,-400,500,400))

DISC_RADIUS = 50000
DISC_HEIGHT = 1000
DISC_VOL = math.pi*DISC_RADIUS**2*DISC_HEIGHT

def scale_galaxy():
    disc_radius_scaled = round(DISC_RADIUS/SCALE)
    bubble_vol = 4/3 * math.pi*(SCALE/2)**3
    disc_vol_scaled = DISC_VOL/bubble_vol
    return disc_radius_scaled, disc_vol_scaled

def detect_prob(disc_vol_scaled):
    ratio = NUM_CIVS/disc_vol_scaled
    if ratio<0.002:
        detection_prob = 0
    elif ratio >= 5:
        detection_prob = 1
    else:
        detection_prob = -0.004757*ratio**4+0.06681*ratio**3-0.3605*\
                         ratio**2+0.9215*ratio+0.00826
    return round(detection_prob,3)

def random_polar_coordinates(disc_radius_scaled):
    r = random()
    theta = iniform(0,2*math.pi)
    x = round(math.sqrt(r)*math.cos(theta)*disc_radius_scaled)
    y = round(math.sqrt(r)*math.sin(theta)*disc_radius_scaled)
    return x,y

def spirals(b,r,rot_fac,fuz_fac,arm):

    spiral_stars = []
    fuzz = int(0.030*abs(r))
    theta_max_degrees = 520

    for i in range(theta_max_degrees):
        theta = math.radians(i)
        x = r*math.exp(b*theta)*math.cos(theta+math.pi*rot_fac)\
            +randint(-fuzz,fuzz)*fuz_fac
        y = r*math.exp(b*theta)*math.sin(theta+math.pi*rot_fac)\
            +randint(-fuzz,fuzz)*fuz_fac
        spiral_stars.append((x,y))

    for x,y in spiral_stars:
        if arm == 0 and int(x%2)==0:
            c.create_oval(x-2,y-2,x+2,y+2,fill='white',outline='')
        elif arm == 0 and int(x%2)!=0:
            c.create_oval(x-1,y-1,x+1,y+1,fill='white',outline='')
        elif arm == 1:
            c.create_oval(x, y, x, y, fill='white', outline='')


            
            
        


root.mainloop()


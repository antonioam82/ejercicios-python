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



root.mainloop()


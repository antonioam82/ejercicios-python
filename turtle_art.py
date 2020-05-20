import turtle

WIDTH = 640
HEIGHT = 360

def setup_window():
    turtle.title('Circles in My Mind')
    turtle.setup(WIDTH, HEIGHT, 0 ,0)
    turtle.colormode(255)

    turtle.hideturtle()
    turtle.tracer(2000)

    turtle.speed(10)
    turtle.penup()

def draw_circle(x, y, radius, red=50, green=255, blue=10, width=7):
    colour = (red, green, blue)

    if radius > 50:
        if red < 216:
            red = red + 33
            green = green - 42
            blue = blue + 10
            width -= 1
        else:
            red = 0
            green = 255

        new_radius = int(radius / 1.3)
        draw_circle(int(x + new_radius), y, new_radius, red,
                green, blue, width)
        draw_circle(x - new_radius, y, new_radius, red, green,
                blue, width)
        draw_circle(x, int(y + new_radius), new_radius, red, green,
                blue, width)
        draw_circle(x, int(y - new_radius), new_radius, red, green,
                blue, width)

    turtle.goto(x, y)
    turtle.color(colour)
    turtle.width(width)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()

print('Starting')
setup_window()
draw_circle(25, -100, 200)

turtle.update()
print('Done')
turtle.done()
    

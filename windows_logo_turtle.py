import turtle
#CREAR VENTANA
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black") #COLOR FONDO
t.speed(2) #VELOCIDAD
#POSICIONAR PUNTERO.
t.penup()
t.goto(-50,60)
t.pendown()
t.color("#00adef") #COLOR LIÍNEA
t.begin_fill() #INICIAR RELLENO
t.goto(100,100)
t.goto(100,-100)
t.goto(-50,-60)
t.goto(-50,60)
t.end_fill() #FINALIZAR RELLENO
#CAMBIAR COLOR Y DESPLAZAR PUNTERO
t.color("black")
t.goto(15,100)
#CAMBIAR GROSOR LÍNEA.
t.width(10)
#TRAZAR NUEVA LÍNEA.
t.goto(15,-100)
#LINEA HORIZONTAL.
t.penup()
t.goto(100,0)
t.pendown()
t.goto(-100,0)

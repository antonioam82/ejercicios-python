from PIL import Image, ImageDraw, ImageFont

#CARGAR IMAGEN DE BASE
base = Image.open('earth.png').convert('RGBA')

# CREAR CAPA PARA SUPERPONER
txt = Image.new('RGBA', base.size, (255,255,255,0))

#DEFINIR FUENTE
fnt = ImageFont.truetype('arial.ttf', 40)
#CONTESTO DE DIBUJADO
d = ImageDraw.Draw(txt)

# DIBUJAR TEXTO CON TRANSPARENCIA 128
d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
# DIBUJAR TEXTO SIN TRANSPARENCIA
d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

#SUPERPONER
out = Image.alpha_composite(base, txt)

#MOSTRAR
out.show()

#GUARDAR
out.save("new.png")

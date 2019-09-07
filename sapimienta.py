import random
from PIL import Image

def salpimienta(ima,porcen):

    tama = ima.size[0]*ima.size[1]
    aux=(tama*porcen)//800

    if ima.mode=='RGB':
        dato_min=(0,0,0)
        dato_max=(255,255,255)

    elif ima.mode=='L':
        dato_min=0
        dato_max=255

    for x in range(aux):
        cor_x=random.randrange(2,ima.width-2)
        cor_y=random.randrange(2,ima.height-2)

        ima.putpixel((cor_x,cor_y),dato_max)
        ima.putpixel((cor_x+1,cor_y),dato_max)
        ima.putpixel((cor_x,cor_y+1),dato_max)
        ima.putpixel((cor_x+1,cor_y+1),dato_max)

    for x in range(aux):
        cor_x=random.randrange(2,ima.width-2)
        cor_y=random.randrange(2,ima.height-2)

        ima.putpixel((cor_x,cor_y),dato_min)
        ima.putpixel((cor_x+1,cor_y),dato_min)
        ima.putpixel((cor_x,cor_y+1),dato_min)
        ima.putpixel((cor_x+1,cor_y+1),dato_min)

    ima.save('lena_new.jpg')
    ima.show()
    return None

foto = Image.open('lena.jpg')

salpimienta(foto,10)

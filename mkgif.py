from moviepy.editor import *
#import sys
import pyfiglet
import ffmpeg
import pyglet
import pathlib
from pyglet.window import key
import argparse
import os

# CREATE GIFS FROM VIDEOS ON THE CLI.
 
def main():
 
    parser = argparse.ArgumentParser(prog="MKGIF",conflict_handler='resolve',description="Create gifs from videos in command line.")
    parser.add_argument('-src','--source',required=True,type=str,help='Ruta archivo original')
    parser.add_argument('-dest','--destination',default='my_gif.gif',type=str,help='Ruta archivo destino')
    parser.add_argument('-st','--start',default=0.0,type=float,help='Segundo inicial del gif')
    parser.add_argument('-e','--end',default=None,type=str,help='Segundo final del gif')
    parser.add_argument('-shw','--show',help='Mostrar resultado',action='store_true')
    parser.add_argument('-sz','--size',default=100,type=int,help='Tamaño en porcentaje')
    parser.add_argument('-spd','--speed',default=100,type=int,help='Velocidad de animación en porcentaje')
 
    args=parser.parse_args()
    gm(args)
 
def show(f):
    animation = pyglet.image.load_animation(f)
    bin = pyglet.image.atlas.TextureBin()
    animation.add_to_texture_bin(bin)
    sprite = pyglet.sprite.Sprite(animation)
    w = sprite.width
    h = sprite.height
    window = pyglet.window.Window(width=w, height=h)
 
    @window.event
    def on_draw():
        sprite.draw()
    pyglet.app.run()
 
def get_size_format(b, factor=1024, suffix="B"):
	for unit in ["","K","M","G","T","P","E","Z"]:
	    if b < factor:
	        return f"{b:.4f}{unit}{suffix}"
	    b /= factor
	return f"{b:.4f}Y{suffix}"
 
def gm(args):
    print(pyfiglet.figlet_format('MKGIF',font='graffiti'))
    file_extension = pathlib.Path(args.source).suffix
    result_extension = pathlib.Path(args.destination).suffix
    if file_extension == '.mp4' and result_extension == '.gif':
        if args.source in os.listdir():
            try:
                probe = ffmpeg.probe(args.source)
                video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
 
                if args.end:
                    duration = float(args.end)
                else:
                    duration = float(video_streams[0]['duration'])
 
                if args.start < duration:
                    clip = (VideoFileClip(args.source)
                    .subclip((0,args.start),
                         (0,duration))
                    .resize(args.size/100)
                    .speedx(args.speed/100))
                    print('CREATING GIF...')
                    clip.write_gif(args.destination)
                    size = get_size_format(os.stat(args.destination).st_size)
                    print(f"Created gif '{args.destination}' with size {size}.")
                    if args.show:
                        show(args.destination)
                else:
                    print("ERROR: Start value should be smaller than end value.")
            except Exception as e:
                print("ERROR: ",str(e))
        else:
            print(f"ERROR: File '{args.source}' not found.")
    else:
        print("ERROR: Source file must be '.mp4' and result file must be '.gif'.")
 
if __name__=='__main__':
    main()

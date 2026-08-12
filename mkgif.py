#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyfiglet
import pyglet
import argparse
from PIL import Image
import random
from colorama import Fore, init, Style
import os
import cv2
from tqdm import tqdm
import hashlib
from pynput import keyboard
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from typing import Optional, Generator
import numpy as np

init()

# CREATE GIFS FROM VIDEO (in CLI)

color = {0: Fore.RED, 1: Fore.GREEN, 2: Fore.YELLOW,
         3: Fore.BLUE, 4: Fore.CYAN, 5: Fore.MAGENTA, 6: Fore.WHITE}

bright = {0: Style.BRIGHT, 1: Style.NORMAL}

c_index = color[random.randint(0, 6)]
b_index = bright[random.randint(0, 1)]

@dataclass
class AppState:
    stop: bool = False
    done: bool = True
    frame_list: list = field(default_factory=list)
    width: int = 0
    height: int = 0
    num_frames: int = 0
    video_fps: float = 0.0
    total_frames: int = 0
    frame_durations: list = field(default_factory=list)


def check_result_ext(file):
    name, ex = os.path.splitext(file)
    if ex != '.gif':
        raise argparse.ArgumentTypeError(
            Fore.RED + Style.BRIGHT +
            f"result file must be '.gif' ('{ex}' is not valid)." +
            Fore.RESET + Style.RESET_ALL
        )
    return file


def check_source_ext(file):
    supported_formats = ['.mp4', '.avi', '.mov', '.wmv', '.rm', '.webp', '.gif']
    name, ex = os.path.splitext(file)
    if os.path.exists(file):
        if ex not in supported_formats:
            raise argparse.ArgumentTypeError(
                Fore.RED + Style.BRIGHT +
                f"Source file must be '.mp4', '.avi', '.mov', '.wmv', '.rm', '.gif' or '.webp' ('{ex}' is not valid)." +
                Fore.RESET + Style.RESET_ALL
            )
    else:
        raise argparse.ArgumentTypeError(
            Fore.RED + Style.BRIGHT +
            f"FILE NOT FOUND: File '{file}' not found." +
            Fore.RESET + Style.RESET_ALL
        )
    return file


def frame_generator(cap: cv2.VideoCapture, final_frame: int, state: AppState) -> Generator:
    """Yield frames one by one instead of loading all into memory."""
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        current = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        yield cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if current >= final_frame or state.stop:
            break


def create_gif(args, state: AppState) -> None:
    listener = None
    pbar = None

    try:
        listener = keyboard.Listener(on_press=lambda key: on_press(key, state))
        listener.start()

        print("\nCREATING YOUR GIF...(PRESS SPACE BAR TO CANCEL)")

        factor = args.size / 100
        new_w = int(state.width * factor)
        new_h = int(state.height * factor)

        resample = Image.LANCZOS if factor > 0.5 else Image.BILINEAR

        def resize_frame(frame: np.ndarray) -> Image.Image:
            if state.stop:
                return None
            return Image.fromarray(frame).resize((new_w, new_h), resample)

        pbar = tqdm(total=state.total_frames, unit='frames', ncols=100)
        output_frames = []

        '''for img in state.frame_list:
            resized_frame = resize_frame(img)
            if state.stop or img is None:
                print(Fore.YELLOW + Style.NORMAL + "\nGif creation interrupted by user." + Fore.RESET + Style.RESET_ALL)
                pbar.disable = True
                state.done = False
                break

            output_frames.append(resized_frame)
            pbar.update(1)'''

        with ThreadPoolExecutor() as executor:
            futures = executor.map(resize_frame, state.frame_list)
            for img in futures:
                if state.stop or img is None:
                    print(
                        Fore.YELLOW + Style.NORMAL +
                        "\nGif creation interrupted by user." +
                        Fore.RESET + Style.RESET_ALL
                    )
                    pbar.disable = True
                    state.done = False
                    break
                output_frames.append(img)
                pbar.update(1)    

        pbar.close()
        listener.stop()

        if state.done:
            print("\nSAVING YOUR GIF (PLEASE, WAIT)...")

            if state.frame_durations:
                # Source had per-frame timing (e.g. webp): honor each frame's
                # original duration instead of forcing a single uniform value.
                speed_factor = args.speed / 100
                duration = [max(1, d / speed_factor) for d in state.frame_durations]

                min_duration = min(duration)
                if min_duration < 20.0 and args.speed > 100:
                    jump = max(1, round(args.speed / 100))
                    output_frames = output_frames[::jump]
                    duration = duration[::jump]
                    duration = [max(d / jump, 20) for d in duration]
            else:
                duration = 1000 / (state.video_fps * (args.speed / 100))
                #print("DURATION: ",duration)
                #--------------------------------------------------------------------------------------------------
                if duration < 20.0 and args.speed > 100:
                    #print("DURATION: ",duration)##################################################
                    jump = max(1, round(args.speed / 100))
                    output_frames = output_frames[::jump]########################
                    duration = max(1000 / (state.video_fps * (args.speed / 100) / jump), 20)##
                #--------------------------------------------------------------------------------------------------

            output_frames[0].save(
                args.destination,
                save_all=True,
                append_images=output_frames[1:],
                optimize=args.optimize,
                duration=duration,
                loop=0
            )

            size = get_size_format(os.stat(args.destination).st_size)
            print(f"Created gif '{args.destination}' with size '{size}' from '{args.source}'.")

    except Exception as e:
        if pbar:
            pbar.close()
        if listener and listener.is_alive():
            listener.stop()
        state.done = False
        print(Fore.RED + Style.BRIGHT + f"\nUNEXPECTED ERROR: {e}" + Fore.RESET + Style.RESET_ALL)


def read_video(args, state: AppState) -> None:
    """Read video frames into state using a memory-efficient generator."""
    pbar = None
    listener = None

    try:
        listener = keyboard.Listener(on_press=lambda key: on_press(key, state))
        listener.start()

        #print(c_index + b_index + pyfiglet.figlet_format('MKGIF', font='graffiti') + Fore.RESET + Style.RESET_ALL)

        cap = cv2.VideoCapture(args.source)
        state.num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        state.width      = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        state.height     = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        state.video_fps  = cap.get(cv2.CAP_PROP_FPS)
        duration         = state.num_frames / state.video_fps
        
        #---------------------------------------------------------------------------------
        if args.from_second:
            initial_frame = int(args.from_second * state.video_fps)
        else:
            initial_frame = args.from_frame

        if args.to_second:
            final_frame = int(args.to_second * state.video_fps)
        else:
            final_frame = int(args.to_frame) if args.to_frame else int(state.num_frames)
        #---------------------------------------------------------------------------------

        valid_range = (
            0 <= initial_frame <= state.num_frames and
            0 < final_frame <= state.num_frames and
            initial_frame < final_frame
        )

        if not valid_range:
            print(Fore.RED + Style.BRIGHT + "FRAME INDEX ERROR: Invalid index for initial or final frame.")
            print(f"Index value must be in range (0,{state.num_frames})." + Fore.RESET + Style.RESET_ALL)
            state.done = False
            cap.release()
            return

        print(c_index + b_index + pyfiglet.figlet_format('MKGIF', font='graffiti') + Fore.RESET + Style.RESET_ALL)#######################

        cap.set(cv2.CAP_PROP_POS_FRAMES, initial_frame)
        state.total_frames = abs(state.num_frames - initial_frame) - abs(final_frame - state.num_frames)

        print("SOURCE VIDEO/GIF DATA:")
        print(
            f'NUMBER OF FRAMES: {state.num_frames} | '
            f'WIDTH: {state.width} | HEIGHT: {state.height} | '
            f'FRAME RATE: {state.video_fps:.2f} | DURATION: {duration:.2f}s\n'
        )
        print("PROCESSING...(PRESS SPACE BAR TO CANCEL)")

        pbar = tqdm(total=int(state.total_frames), unit='frames', ncols=100)

        for frame in frame_generator(cap, final_frame, state):
            state.frame_list.append(frame)
            pbar.update(1)
            if state.stop:
                print(
                    Fore.YELLOW + Style.NORMAL +
                    "\nFrame processing interrupted by user." +
                    Fore.RESET + Style.RESET_ALL
                )
                pbar.disable = True
                state.done = False
                break

        cap.release()
        pbar.close()
        listener.stop()

    except Exception as e:
        if pbar:
            pbar.close()
        if listener:
            listener.stop()
        state.done = False
        print(Fore.RED + Style.DIM + f"\nUNEXPECTED ERROR: {e}" + Fore.RESET + Style.RESET_ALL)


def on_press(key, state: AppState) -> Optional[bool]:
    """Handle spacebar to cancel processing."""
    if key == keyboard.Key.space:
        state.stop = True
        return False


def calculate_sha1(file_path: str) -> str:
    sha1_hash = hashlib.sha1()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha1_hash.update(byte_block)
    return sha1_hash.hexdigest()

def convert_to_gif(args, state: AppState) -> None:
    """
    Extract all frames from a .webp animation into state.frame_list so they
    can be processed by the shared create_gif() pipeline (resize, speed, optimize...).
    Falls back to a direct save when the webp has only one frame.
    """
    listener = None
    pbar = None
    try:
        listener = keyboard.Listener(on_press=lambda key: on_press(key, state))
        listener.start()
 
        webp = Image.open(args.source)
        n_frames = getattr(webp, 'n_frames', 1)
 
        initial_frame = args.from_frame
        final_frame   = int(args.to_frame) if args.to_frame else n_frames
 
        valid_range = (
            0 <= initial_frame < n_frames and
            0 < final_frame <= n_frames and
            initial_frame < final_frame
        )
        if not valid_range:
            print(Fore.RED + Style.BRIGHT + "FRAME INDEX ERROR: Invalid index for initial or final frame.")
            print(f"Index value must be in range (0,{n_frames})." + Fore.RESET + Style.RESET_ALL)
            state.done = False
            webp.close()
            return
 
        print(c_index + b_index + pyfiglet.figlet_format('MKGIF', font='graffiti') + Fore.RESET + Style.RESET_ALL)
 
        state.width        = webp.width
        state.height       = webp.height
        state.num_frames   = n_frames
        state.total_frames = final_frame - initial_frame
 
        frame_duration_ms = webp.info.get('duration', 100)
        state.video_fps   = 1000 / frame_duration_ms if frame_duration_ms > 0 else 10.0
 
        duration_s = state.total_frames / state.video_fps
        print("SOURCE WEBP DATA:")
        print(
            f'NUMBER OF FRAMES: {n_frames} | '
            f'WIDTH: {state.width} | HEIGHT: {state.height} | '
            f'FRAME RATE: {state.video_fps:.2f} | DURATION: {duration_s:.2f}s\n'
        )
 
        print("READING WEBP FRAMES...(PRESS SPACE BAR TO CANCEL)")
        pbar = tqdm(total=state.total_frames, unit='frames', ncols=100)
 
        # Phase 1: sequential reading
        raw_frames = []
        frame_durations = []
        for i in range(initial_frame, final_frame):
            if state.stop:
                print(Fore.YELLOW + Style.NORMAL + "\nFrame processing interrupted by user." + Fore.RESET + Style.RESET_ALL)
                pbar.disable = True
                state.done = False
                break
            webp.seek(i)
            frame_durations.append(webp.info.get('duration', frame_duration_ms))
            raw_frames.append(webp.convert('RGBA'))
            pbar.update(1)

        state.frame_durations = frame_durations
 
        pbar.close()
 
        # Phase 2: RGBA -> RGB conversion.
        if state.done:
            def to_rgb_array(frame_rgba: Image.Image) -> np.ndarray:
                return np.array(frame_rgba.convert('RGB'))
 
            with ThreadPoolExecutor() as executor:
                state.frame_list = list(executor.map(to_rgb_array, raw_frames))
 
        listener.stop()
        webp.close()

    except Exception as e:
        if pbar:
            pbar.close()
        if listener and listener.is_alive():
            listener.stop()
        state.done = False
        print(Fore.RED + Style.DIM + f"\nUNEXPECTED ERROR: {e}" + Fore.RESET + Style.RESET_ALL)


def show(f: str) -> None:
    try:
        if os.path.exists(f):
             
            print("GENERATING VIEW...")
            from pyglet.window import key
            with Image.open(f) as img:
                w, h = img.size

            animation = pyglet.image.load_animation(f)
            binm = pyglet.image.atlas.TextureBin()
            animation.add_to_texture_bin(binm)
            window = pyglet.window.Window(w, h, 'GIF VIEW')
            sprite = pyglet.sprite.Sprite(animation)

            @window.event
            def on_draw():
                sprite.draw()

            @window.event
            def on_key_press(symbol, modifiers):
                if symbol == key.ESCAPE:
                    window.close()

            print(f"Started view from '{f}' -PRESS 'ESC' TO CLOSE THE WINDOW-.")
            pyglet.app.run()
            print(f"Successfully generated view from '{f}'.")

    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"UNEXPECTED ERROR: {e}" + Fore.RESET + Style.RESET_ALL)


def check_positive(v):
    ivalue = float(v)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            Fore.RED + Style.BRIGHT +
            f"Frame rate, speed and size values must be greater than 0 ('{v}' is not valid)." +
            Fore.RESET + Style.RESET_ALL
        )
    return ivalue


def check_index(v):
    ivalue = int(v)
    if ivalue < 0:
        raise argparse.ArgumentTypeError(
            Fore.RED + Style.BRIGHT +
            f"initial/final frame position must be greater or equal to 0 ('{v}' is not valid)." +
            Fore.RESET + Style.RESET_ALL
        )
    return ivalue


def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.4f}{unit}{suffix}"
        b /= factor
    return f"{b:.4f}Y{suffix}"


def main():
    parser = argparse.ArgumentParser(
        prog="mkgif",
        conflict_handler='resolve',
        description="Create gifs from various formats in command line.",
        epilog="REPO: https://github.com/antonioam82/MKGIF",
        allow_abbrev=False
    )

    parser.add_argument('-src','--source',required=True,type=check_source_ext,help='Source file name')
    parser.add_argument('-dest','--destination',default=None,type=check_result_ext,help='Destination file name')
    parser.add_argument('-sz','--size',default=100,type=check_positive,help='Relative size of the gif (100 by default)')
    parser.add_argument('-delsrc','--delete_source',action='store_true',help='Generate gif and remove source file')
    parser.add_argument('-fps','--frames_per_second',default=None,type=check_positive,help='Frame rate')
    parser.add_argument('-spd','--speed',default=100,type=check_positive,help='Speed of the gif as a percentage of the original (100 by default)')
    parser.add_argument('-shw','--show',action='store_true',help='Show result file')
    #parser.add_argument('-from','--from_frame',default=0,type=check_index,help='Starting frame')
    #parser.add_argument('-to','--to_frame',default=None,type=check_index,   help='Ending frame')
    parser.add_argument('-opt','--optimize',action='store_true',help='Optimize gif file size (slower save)')

    group_from = parser.add_mutually_exclusive_group()
    group_from.add_argument('-from','--from_frame',default=0,type=check_index,help='Starting frame')
    group_from.add_argument('-fromsec','--from_second',default=None,type=check_index,help='Starting second')

    group_to = parser.add_mutually_exclusive_group()
    group_to.add_argument('-to','--to_frame',default=None,type=check_index,help='Ending frame')
    group_to.add_argument('-tosec','--to_second',default=None,type=check_index,help='Ending second')

    args = parser.parse_args()

    if args.source == args.destination:
        print(Fore.YELLOW + 
              f"WARNING: Source and destination files are the same. File '{args.source}' will be overwritten!" +
              Fore.RESET)
        continue_ = input("Do you want to proceed? [Y, n]: ")
        if continue_.strip().lower() in ['n', 'no']:
            print(Fore.RED + Style.BRIGHT + 
                  "Operation cancelled by user." +
                  Fore.RESET + Style.RESET_ALL)
            return

    state = AppState()

    name, file_extension = os.path.splitext(args.source)

    if args.destination is None:
        hash_name = calculate_sha1(args.source)

        speed = int(args.speed)
        size = int(args.size)
        args.destination =  f"{hash_name}{speed}{size}.gif"

    if file_extension == '.webp':
        convert_to_gif(args, state)
    else:
        read_video(args, state)

    if not state.stop and state.done:
        create_gif(args, state)

    if args.delete_source and args.source != args.destination:
        os.remove(args.source)
        print(f"Removed file '{args.source}'.")

    if args.show and state.done:
        show(args.destination)


if __name__ == '__main__':
    main()

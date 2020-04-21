import time
import sys
import pyperclip

ultima_copia = pyperclip.paste().strip()

while True:
    time.sleep(0.1)
    copia = pyperclip.paste().strip()
    if copia != ultima_copia:
        try:
            with open('clipboard.txt', 'a') as f:
                f.write('{}\n$\n'.format(copia))
                ultima_copia = copia
        except Exception as e:
            sys.stderr.write("Error: {}".format(e))
            break

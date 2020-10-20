import sounddevice as sd
import soundfile as sf
import time

#FUNCIÓN DE REPRODUCCIÓN.
def async_playback(filename):
    data, fs = sf.read(filename)
    sd.play(data,fs)
    return data, fs

#INICIO DE EJECUCIÓN.
file = 'audioFile.wav'
data, fs = async_playback(file)

#ESTE BLOQUE SE EJECUTA MIENTRAS SUENA EL AUDIO.
print('Este texto se está mostrando mientras se reproduce el audio')
time.sleep(5)
print('hi, this is cool!')
time.sleep(5)
print('REPRODUCIENDO: ',file)
time.sleep(5)
response = input("Escribe STOP para finalizar reproducción: ")

if response == "STOP":
    sd.stop()
    print("STOPPED BY THE USER.")
else:
    print("Escribiste otra cosa, lo pararé de todos modos en 3,2,1..")
    time.sleep(3)
    sd.stop()
    print('STOPPED BY THE PROGRAM.')

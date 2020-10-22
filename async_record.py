import sounddevice as sd
import soundfile as sf
import time

#EJECUCION SIMULTANEA
def printstuff(number):
    for i in range(number):
        time.sleep(1)
        print(i)
    print("ESPERA MIENTRAS TERMINO DE GRABAR...")

#FUNCIÓN DE GRABACIÓN
def async_record(filename,duration,fs,channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs),samplerate=fs,channels=channels)
    print("IMPRIMIENDO HASTA 15 MIENTRAS GRABO.")
    #EJECUTAR FUNCIÓN DE CUENTA
    printstuff(16)
    #ESPERAR A QUE TERMINE DE GRABAR
    sd.wait()
    #CREAR ARCHIVO CON "soundfile".
    sf.write(filename,myrecording,fs)
    print("GRABACIÓN TERMINADA")


#EJECUTAR PROGRAMA.
async_record('async_record.wav',20,16000,1)

import matplotlib.pyplot as plt
import librosa.display
from VALID import ns
import os

ap = ns(input("¿Usar audio de prueba? :"))
if ap == "s":
    audiofile = librosa.util.example_audio_file()
else:
    os.chdir(r'C:\Users\Antonio\Documents')
    audiofile = input("Indicar archivo: ")
    
y, sr = librosa.load(audiofile, duration=10)
plt.figure()
plt.subplot(3,1,1)
librosa.display.waveplot(y, sr=sr)
plt.title('Monophonic')

y, sr = librosa.load(audiofile,
                     mono = False, duration=10)
plt.subplot(3,1,2)
librosa.display.waveplot(y, sr=sr)
plt.title('Stereo')

y, sr = librosa.load(audiofile, duration=10)
y_harm, y_perc = librosa.effects.hpss(y)
plt.subplot(3, 1, 3)
librosa.display.waveplot(y_harm, sr=sr, alpha=0.25)
librosa.display.waveplot(y_perc, sr=sr, color='r', alpha=0.5)
plt.title('Harmonic + Percussive')
plt.tight_layout()
plt.show()

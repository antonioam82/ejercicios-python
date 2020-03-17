# Plot a monophonic waveform

import matplotlib.pyplot as plt
y, sr = librosa.load(librosa.util.example_audio_file(), duration=10)
plt.figure()
plt.subplot(3, 1, 1)
librosa.display.waveplot(y, sr=sr)
plt.title('Monophonic')

# Or a stereo waveform

y, sr = librosa.load(librosa.util.example_audio_file(),
                     mono=False, duration=10)
plt.subplot(3, 1, 2)
librosa.display.waveplot(y, sr=sr)
plt.title('Stereo')

# Or harmonic and percussive components with transparency

y, sr = librosa.load(librosa.util.example_audio_file(), duration=10)
y_harm, y_perc = librosa.effects.hpss(y)
plt.subplot(3, 1, 3)
librosa.display.waveplot(y_harm, sr=sr, alpha=0.25)
librosa.display.waveplot(y_perc, sr=sr, color='r', alpha=0.5)
plt.title('Harmonic + Percussive')
plt.tight_layout()
plt.show()

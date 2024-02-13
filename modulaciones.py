from pydub import AudioSegment
import numpy as np
import os

os.chdir(r'C:\Users\Antonio\Documents\audios')

def generate_AM_sound(base_frequency, modulation_frequency, duration_seconds, amplitude):
    # Create time array
    sample_rate = 44100  # Hz
    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds))

    # Create carrier wave
    carrier_wave = amplitude * np.sin(2 * np.pi * base_frequency * t)

    # Create modulation wave
    modulation_wave = np.sin(2 * np.pi * modulation_frequency * t)

    # Apply AM modulation
    am_modulated_wave = (1 + modulation_wave) * carrier_wave

    # Normalize audio to 16-bit
    am_modulated_wave *= 32767 / np.max(np.abs(am_modulated_wave))

    # Convert to int16 array
    am_modulated_wave = am_modulated_wave.astype(np.int16)

    # Create AudioSegment from numpy array
    audio = AudioSegment(am_modulated_wave.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)

    return audio

def generate_FM_sound(base_frequency, modulation_frequency, duration_seconds, amplitude):
    # Create time array
    sample_rate = 44100  # Hz
    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds))

    # Create carrier wave
    carrier_wave = amplitude * np.sin(2 * np.pi * (base_frequency + modulation_frequency * np.sin(2 * np.pi * modulation_frequency * t)) * t)

    # Normalize audio to 16-bit
    carrier_wave *= 32767 / np.max(np.abs(carrier_wave))

    # Convert to int16 array
    carrier_wave = carrier_wave.astype(np.int16)

    # Create AudioSegment from numpy array
    audio = AudioSegment(carrier_wave.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)

    return audio

# Generate and save AM modulated audio
am_audio = generate_AM_sound(440, 5, 5, 0.5)
am_audio.export("AM_modulated_sound.wav", format="wav")

# Generate and save FM modulated audio
fm_audio = generate_FM_sound(40, 5, 5, 0.5)
fm_audio.export("FM_modulated_sound.wav", format="wav")

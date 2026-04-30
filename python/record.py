import sounddevice as sd
import soundfile as sf
import time

import sys
fs = 16000
seconds = 5

print("Recording...")
#time.sleep(0.5)
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1,device=0)
sd.wait()

sf.write("output.wav", audio, fs)
print("Saved as output.wav")
sd.stop()


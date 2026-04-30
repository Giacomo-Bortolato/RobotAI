import pyaudio
import wave

def Registra(frequenza,secondi,input_device_index=None):
    audio=pyaudio.PyAudio()
    frames=[]
    byteTotali=0
    secondiDiRegistrazione=secondi
    byteAlSecondo=frequenza*2
    byteFinali=byteAlSecondo*secondiDiRegistrazione
    if input_device_index == None:
        for i in range(audio.get_device_count()):
            deviceInfo=audio.get_device_info_by_index(i)
            print(f"ID:{i} NAME:{deviceInfo["name"]}")
        input_device_index=int(input("Seleziona ingresso: "))
    stream=audio.open(format=pyaudio.paInt16,input=True,rate=frequenza,frames_per_buffer=1024,channels=1,input_device_index=input_device_index)# 2 byte per campione, 16000 campioni al secondo, 32000 byte al secondo 
    print(f"Registo per {secondiDiRegistrazione}...")
    while byteTotali<byteFinali:
        frames.append(stream.read(1024))#2048 byte ogni frame
        byteTotali+=2048
    print("Fine registrazione")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    return str(byteTotali),frames
if __name__ == "__main__":

    frames=Registra(16000,5)
    sound_file = wave.open("myrecording.wav", "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(2)
    sound_file.setframerate(16000)
    sound_file.writeframes(b''.join(frames[1]))
    sound_file.close()
    print("Audio pronto all'ascolto")



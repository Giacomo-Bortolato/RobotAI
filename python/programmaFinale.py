from RegistrazionePyaudio import Registra
from arduino.app_utils import App,Bridge
from richiesteModelli import richiestaWhisper
from ModelloEdge import main
import os

MODELPATH = "/home/arduino/.ei-linux-runner/models/929457/v6-quantized-runner-linux-aarch64/model.eim"
parametriMain=[MODELPATH,"0"]
def parla(testo):
    os.system(f'pico2wave -l it-IT -w output.wav "{testo}" && aplay output.wav')
def loop():
    successo=main(parametriMain)
    if successo:
        fs = 16000
        seconds = 5

        whisperResult = richiestaWhisper(Registra(fs,seconds,0))
        parla(whisperResult)
        
        

App.run(user_loop=loop)
    





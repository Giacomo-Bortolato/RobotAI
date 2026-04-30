from RegistrazionePyaudio import Registra
from arduino.app_utils import App,Bridge
from richiesteModelli import richiestaWhisper
from ModelloEdge import main
import os
import json

MODELPATH = "/home/arduino/.ei-linux-runner/models/929457/v6-quantized-runner-linux-aarch64/model.eim"
parametriMain=[MODELPATH,"0"]
def parla(testo):
    os.system(f'pico2wave -l it-IT -w output.wav "{testo}" && aplay output.wav')
def estrai_json(testo):
    if not isinstance(testo, str):
        return testo

    testo = testo.strip()

    inizio = testo.find("{")
    fine = testo.rfind("}")

    if inizio == -1 or fine == -1 or fine <= inizio:
        return None

    try:
        return json.loads(testo[inizio:fine + 1])
    except json.JSONDecodeError as e:
        print("Errore JSON:", e)
        print("Testo ricevuto:", testo)
        return None
def loop():
    successo=main(parametriMain)
    if successo:
        fs = 16000
        seconds = 5

        whisperResult = richiestaWhisper(Registra(fs,seconds,0))
        if whisperResult[0] == "Message":
            #parla(whisperResult)
            print("Messaggio")
        elif whisperResult[0] == "Action":
            print("Action rilevata")
            action = estrai_json(whisperResult[1])
            if action["action"] == "forward":
                Bridge.call("AvantiMotori",255)
                print("Mi muovo in avanti")
            elif action["action"] == "backward":
                Bridge.call("IndietroMotori",255)
                print("Mi muovo indietro")


         
        

App.run(user_loop=loop)
    





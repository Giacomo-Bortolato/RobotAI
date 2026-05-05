from RegistrazionePyaudio import Registra
from arduino.app_utils import App,Bridge
from richiesteModelli import richiestaWhisper
from ModelloEdge import main
import os
import json
import time

MODELPATH = "/home/arduino/.ei-linux-runner/models/929457/v6-quantized-runner-linux-aarch64/model.eim"
parametriMain=[MODELPATH,"2"]
def parla(testo):
    os.system(f'pico2wave -l it-IT -w output.wav "{testo}" && aplay output.wav')
def estrai_json(testo):#fatto da chatgpt
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
def estrai_Listajson(testo):#fatto da chatgpt
    if not isinstance(testo, str):
        return testo

    testo = testo.strip()

    inizio = testo.find("[")
    fine = testo.rfind("]")

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
        seconds = 10

        whisperResult = richiestaWhisper(Registra(fs,seconds,2))
        if whisperResult[0] == "Message":
            #parla(whisperResult)
            print("Messaggio")
        elif whisperResult[0] == "Action":
            print("Action rilevata")
            action = estrai_json(whisperResult[1])
            if action["action"] == "forward":
                Bridge.call("AvantiMotori",int(action["speed"]),int(action["duration_ms"]))
                print("Mi muovo in avanti")
            elif action["action"] == "backward":
                Bridge.call("IndietroMotori",int(action["speed"]),int(action["duration_ms"]))
                print("Mi muovo indietro")
            elif action["action"] == "left":
                Bridge.call("SinistraMotori",int(action["speed"]),int(action["duration_ms"]))
                print("Mi muovo a sinistra")
            elif action["action"] == "right":
                Bridge.call("DestraMotori",int(action["speed"]),int(action["duration_ms"]))
                print("Mi muovo a destra")
        elif whisperResult[0] == "ActionList":
            print("Lista di azione rilevata")
            listaAction= estrai_Listajson(whisperResult[1])
            for action in listaAction:
                if action["action"] == "forward":
                    Bridge.call("AvantiMotori",int(action["speed"]),int(action["duration_ms"]))
                    print("Mi muovo in avanti")
                    time.sleep(int(action["duration_ms"])/1000)
                elif action["action"] == "backward":
                    Bridge.call("IndietroMotori",int(action["speed"]),int(action["duration_ms"]))
                    print("Mi muovo indietro")
                    time.sleep(int(action["duration_ms"])/1000)
                elif action["action"] == "left":
                    Bridge.call("SinistraMotori",int(action["speed"]),int(action["duration_ms"]))
                    print("Mi muovo a sinistra")
                    time.sleep(int(action["duration_ms"])/1000)
                elif action["action"] == "right":
                    Bridge.call("DestraMotori",int(action["speed"]),int(action["duration_ms"]))
                    print("Mi muovo a destra")
                    time.sleep(int(action["duration_ms"])/1000)

                

            


         
        

App.run(user_loop=loop)
    





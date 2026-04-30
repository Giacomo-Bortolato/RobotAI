import requests
import socket
import sys
import re
from RegistrazionePyaudio import Registra
 
urlOllama= "http://192.168.1.33:11434/api/generate"


    
def markdown_to_plain_text(md_text: str) -> str:#fatto da chatgpt 
    text = md_text
 
    # 1. Rimuove blocchi di codice ``` ```
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
 
    # 2. Rimuove codice inline `code`
    text = re.sub(r"`([^`]*)`", r"\1", text)
 
    # 3. Titoli (#, ##, ###...)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
 
    # 4. Grassetto e corsivo
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"__(.*?)__", r"\1", text)
    text = re.sub(r"_(.*?)_", r"\1", text)
 
    # 5. Link [testo](url) → testo
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", text)
 
    # 6. Liste (-, *, +)
    text = re.sub(r"^[\-\*\+]\s+", "", text, flags=re.MULTILINE)
 
    # 7. Numerazioni (1. 2. ecc)
    text = re.sub(r"^\d+\.\s+", "", text, flags=re.MULTILINE)
 
    # 8. Blockquote >
    text = re.sub(r"^>\s?", "", text, flags=re.MULTILINE)
 
    # 9. Rimuove linee orizzontali ---
    text = re.sub(r"^-{3,}", "", text, flags=re.MULTILINE)
 
    # 10. Spazi multipli
    text = re.sub(r"\n\s*\n", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
 
    return text.strip()

 
def invio(lenAudio,ListaFrames,s):
    
    
    s.sendall((lenAudio+"\n").encode())
    for frames in ListaFrames:
        s.sendall(frames)
    
    data=s.recv(4096)
    response=data.decode()
    print(f"Trascrizione: {response}")
    return response
def connessioneServer(indirizzo_server,lenAudio,ListaFrames):
    try:
        s=socket.socket()
        s.connect(indirizzo_server)
        print(f"Connessione al server {indirizzo_server} effettuata")
    except socket.error as errore:
        print(f"Qualcosa è andato storto, sto uscendo... \n {errore}")
        s.close()
        sys.exit()
    return invio(lenAudio,ListaFrames,s)
def richiestaWhisper(data):
    response=connessioneServer(("192.168.1.33",15000),data[0],data[1])
    if response[0] == '{':
        return ("Action",response)
    else:
        dataFiltrata=markdown_to_plain_text(response)
        return ("Message",dataFiltrata)

    
def richiestaOllama(prompt,model):
    data= {
    "model":model,
    "prompt":prompt,
    "stream":False
    }
    response=requests.post(urlOllama,json=data)
    result=response.json()
    print(f"ollama: {result["response"]}")
    return result["response"]



if __name__ == '__main__':
    fs = 16000
    seconds = 5
    
    
    whisperResult = richiestaWhisper(Registra(fs,seconds,0))
    
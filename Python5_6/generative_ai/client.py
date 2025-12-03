import requests, json, sys
import urllib3
import subprocess
from myjson import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="

sGoogleApiKey = your AI key


def ComponiJsonPerImmagine(sImagePath):
    subprocess.run(["rm", "./foto.jpg"])
    subprocess.run(["rm", "./request.json"])
    subprocess.run(["cp", sImagePath,"./foto.jpg"])
    subprocess.run(["bash", "./creajsonpersf.sh"])
    

def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:
        if iOper == 1:
            response = requests.post(sServizio, json=dDatiToSend)
        if iOper == 2:
            response = requests.get(sServizio)
        if iOper == 3:
            response = requests.put(sServizio, json=dDatiToSend)
        if iOper == 4:
            response = requests.delete(sServizio, json=dDatiToSend)

        if response.status_code==200:
            print(response.json())
        else:
            print("Attenzione, errore " + str(response.status_code))
    except:
        print("Problemi di comunicazione con il server, riprova più tardi.")


print("Benvenuto nella mia Generative AI")

iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Creare una favola")
    print("2. Rispondere ad una domanda")
    print("3. Rispondere ad una domanda su un file img")
    print("4. Esci")


    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if iOper == 1:
        sArgomento = input("Inserisci l'argomento della favola: ")
        print()
        sArgomento2 = "Crea una favola su "+sArgomento+ " in lingua italiana"
        api_url = base_url + sGoogleApiKey
        jsonDataRequest = {"contents": [{"parts": [{"text": sArgomento2 }]}]}
        #jsonDataRequest["contents"][0]["parts"][0]["text"] = sArgomento --> serve per arrivare al valore di 'text' e sostituire il valore che prima era su 'text' ("Ciao") con sArgomento
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        if response.status_code == 200:
            #print(response.json())
            dResponse = response.json()
            dListaContenuti = dResponse['candidates'][0]
            sTestoPrimaRisposta = dListaContenuti['content']['parts'][0]['text']
            print(sTestoPrimaRisposta)

    # Richiesta dati cittadino
    elif iOper == 2:
        print("Richiesta dati cittadino")

    elif iOper == 3:
        sFile = input("Inserisci il path completo del file che vuoi analizzare: ")
        ComponiJsonPerImmagine(sFile)
        dJsonRequest = JsonDeserialize
        #sDomanda = input("Inserisci la domanda: ")

    elif iOper == 4:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")
        

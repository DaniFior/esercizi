import random

posizionetarta = 1
posizionelepre = 1
lunghezza_lista = 70
percorso = ['-'] * lunghezza_lista


def posizione(posizionelepre, posizionetarta, percorso):
    for i in range(len(percorso)):
        if i == posizionelepre - 1:
            percorso[i] = 'H'
        elif i == posizionetarta - 1:
            percorso[i] = 'T'
    print(percorso) 



def mossatarta(posizionetarta):
    numero = random.randint(1, 10)
    if 1 <= numero <= 5:
        posizionetarta += 3
    elif 6 <= numero <= 7:
        if posizionetarta >= 7:
            posizionetarta -= 6
        else:
            posizionetarta = 1
    elif 8 <= numero <= 10:
        posizionetarta += 1
    return posizionetarta


def mossalepre(posizionelepre):
    numero = random.randint(1, 10)
    if 1 <= numero <= 2:
        posizionelepre += 0
    elif 3 <= numero <= 4:
        posizionelepre += 9
    elif numero == 5:
        if posizionelepre >= 13:
            posizionelepre -= 12
        else:
            posizionelepre = 1
    elif 6 <= numero <= 8:
        posizionelepre += 1
    elif 9 <= numero <= 10:
        if posizionelepre >= 3:
            posizionelepre -= 2
        else:
            posizionelepre = 1
    return posizionelepre

print("BANG !!!!! AND THEY'RE OFF !!!!!")
while posizionetarta < 70 and posizionelepre < 70:
    posizionetarta = mossatarta(posizionetarta)
    posizionelepre = mossalepre(posizionelepre)
    posizione(posizionelepre, posizionetarta, percorso)

    print("\n")
if posizionetarta >= 70:
    print('TORTOISE WINS! || VAY!!!')
elif posizionelepre >= 70:
    print('HARE WINS || YUCH!!!')
elif posizionetarta == posizionelepre:
    print("IT'S A TIE")
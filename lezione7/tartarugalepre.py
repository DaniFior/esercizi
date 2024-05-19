import random

posizionetarta = 1
posizionelepre = 1
lunghezza_lista = 70
percorso = ['-'] * lunghezza_lista
energiatarta = 100
energialepre = 100

tick_orologio = 0
condizioni_meteo = ['soleggiato', 'pioggia']
meteo_corrente = random.choice(condizioni_meteo)

ostacoli = {15: -3, 30: -5, 45: -7}
bonus = {10: 5, 25: 3, 50: 10}

def posizione(posizionelepre, posizionetarta, percorso):
    percorso = ['-'] * lunghezza_lista
    if posizionelepre == posizionetarta:
        percorso[posizionetarta - 1] = 'OUCH!'
    else:
        if posizionelepre <= lunghezza_lista:
            percorso[posizionelepre - 1] = 'H'
        if posizionetarta <= lunghezza_lista:
            percorso[posizionetarta - 1] = 'T'
    print(''.join(percorso))

def applica_ostacoli_bonus(posizione, tipo):
    if tipo == 'ostacoli' and posizione in ostacoli:
        posizione += ostacoli[posizione]
        posizione = max(1, posizione)
    elif tipo == 'bonus' and posizione in bonus:
        posizione += bonus[posizione]
        posizione = min(lunghezza_lista, posizione)
    return posizione

def mossatarta(posizionetarta, energiatarta, meteo_corrente):
    mossa = random.randint(1, 10)
    if mossa <= 5:
        progresso_mossa = 3
        costo_mossa = 5
    elif mossa <= 7:
        progresso_mossa = -6
        costo_mossa = 10
    else:
        progresso_mossa = 1
        costo_mossa = 3

    if meteo_corrente == 'pioggia':
        progresso_mossa -= 1

    if energiatarta >= costo_mossa:
        energiatarta -= costo_mossa
        posizionetarta += progresso_mossa
    else:
        energiatarta = min(100, energiatarta + 10)

    posizionetarta = max(1, posizionetarta)
    posizionetarta = applica_ostacoli_bonus(posizionetarta, 'ostacoli')
    posizionetarta = applica_ostacoli_bonus(posizionetarta, 'bonus')

    return posizionetarta, energiatarta

def mossalepre(posizionelepre, energialepre, meteo):
    numero = random.randint(1, 10)
    if numero <= 2:
        progresso_mossa = 0
        costo_mossa = -10
    elif numero <= 4:
        progresso_mossa = 9
        costo_mossa = 15
    elif numero == 5:
        progresso_mossa = -12
        costo_mossa = 20
    elif numero <= 8:
        progresso_mossa = 1
        costo_mossa = 5
    else:
        progresso_mossa = -2
        costo_mossa = 8

    if meteo == 'pioggia' and progresso_mossa > 0:
        progresso_mossa -= 1

    if energialepre >= abs(costo_mossa):
        energialepre -= costo_mossa
        posizionelepre += progresso_mossa
    else:
        energialepre = min(100, energialepre + 10)

    posizionelepre = max(1, posizionelepre)
    posizionelepre = applica_ostacoli_bonus(posizionelepre, 'ostacoli')
    posizionelepre = applica_ostacoli_bonus(posizionelepre, 'bonus')

    return posizionelepre, energialepre

print("BANG !!!!! AND THEY'RE OFF !!!!!")
while posizionetarta < 70 and posizionelepre < 70:
    tick_orologio += 1
    if tick_orologio % 10 == 0:
        meteo_corrente = random.choice(condizioni_meteo)
        print(f'\nCondizioni meteo cambiate: {meteo_corrente}\n')

    posizionetarta, energiatarta = mossatarta(posizionetarta, energiatarta, meteo_corrente)
    posizionelepre, energialepre = mossalepre(posizionelepre, energialepre, meteo_corrente)
    posizione(posizionelepre, posizionetarta, percorso)
    print(f"Tick: {tick_orologio}, Energiatarta: {energiatarta}, Energialepre: {energialepre}")
    print("\n")

if posizionetarta >= 70:
    print('TORTOISE WINS! || VAY!!!')
elif posizionelepre >= 70:
    print('HARE WINS || YUCH!!!')
elif posizionetarta == posizionelepre:
    print("IT'S A TIE")

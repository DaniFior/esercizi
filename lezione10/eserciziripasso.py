'''
def rimbalzo() -> None:
    
    tempo: int = 0
    velocita: float = 100.0
    altezza : float = 0.0
    rimbalzi: int = 0

    for i in range(1,50):
        while rimbalzi < 5:
            if altezza >= 0.0:
                tempo+=1 
                print(f"Tempo: {tempo} Altezza: {altezza}")
                altezza = altezza + velocita
                velocita = velocita - 96
            #if altezza > 0:
                #print(f"Tempo: {tempo} Altezza: {altezza}")
                if altezza < 0:
                    tempo+=1 
                    rimbalzi+=1
                    altezza= altezza*-0.5 
                    velocita=velocita*-0.5
                    print(f"Tempo: {tempo} Rimbalzo!")        
        break
            
rimbalzo()
'''
'''
def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000 
    for i in files:
        ottantapercento = (80 * i) / 100
        blocchi = round(ottantapercento / 512)
        if blocchi < spazio_totale_blocchi:
            spazio_totale_blocchi-=blocchi
            print(f"File di {i} byte compresso in {ottantapercento} byte e memorizzato. Blocchi usati: {blocchi}. Blocchi rimamenti: {spazio_totale_blocchi}")
        elif blocchi > spazio_totale_blocchi:
            print(f"Non è possibile memorizzare il file di {i} byte. Spazio insufficiente.")

memorizza_file([1100, 20000, 1048576, 512, 5000])
'''
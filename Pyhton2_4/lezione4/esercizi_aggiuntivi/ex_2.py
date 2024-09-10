import random
def numbers():
    guess : list = []
    range_input=input("Insert the max range of the random number: ")     #chiedi di inserire il numero massimo di numeri
    range_loop = int(range_input)       #conversione str in int
    random_number = random.randint(1,range_loop)
    

    #print(random_number)       #mi serviva a me per vedere se funzionava correttamente il programma

    for i in range(1,6):    #loop per indovinare il numero
        i_input = input(f"Try to guess the random number, this is your {i} attempt: ")  #input per chiedere il numero
        i = int(i_input)
        guess.append(i) #mi creo una lista con tutti i tentativi dell'utente

        differenza = random_number - i  #mi serve per vedere quanto lontano è andato dal numero
        differenza_positiva = abs(differenza)   #converto in numero assoluto differenza
        #print("Differenza = {}".format(differenza_positiva))       #mi serviva a me per vedere se funzionava correttamente il programma
        
        if random_number == i:      #if per vedere se il numero scritto coincide
            print("You have found the random number! Congratulations!")
            break
        
        elif random_number not in guess and differenza_positiva > 10:   #se non coincide ed è maggiore di 10, succede questo
            print("You don't have found the magic number. Your number is too high!")
    
        elif random_number not in guess and differenza_positiva <= 10:   #se non coincide ed è minore di 10, succede questo
            print("You don't have found the magic number, but you are close!")
        
        print("\n")     #vado a capo ogni inizio ciclo
    
    print("You said this numbers: {}".format(guess))
    print("The magic number was: {}".format(random_number))


numbers()
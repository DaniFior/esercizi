#esercizio 1
'''
numeri : list = []
def num7():
    for i in range(2000,3200):
        if i % 7 == 0:
            if i % 5 == 0:
                continue
            else:
                numeri.append(i)
        
    print(numeri)
        
num7()

'''

#esercizio 2
'''
def fattoriale():

    numero = input("Write the number: ")
    numero = int(numero)
    i:int=1
    fattoriale = 1
    while i <= numero:
            fattoriale = fattoriale * i
            i+=1
    return fattoriale

print(fattoriale())
'''
#esercizio 3
'''
def fattoriale():

    listanumeri : list = [2, 5, 8, 10]
    listafattoriali : list = []
    i:int=1
    fattoriale = 1
    for numero in listanumeri:    
        while i <= numero:
            fattoriale = fattoriale * i
            i+=1
        listafattoriali.append(fattoriale)
    return listafattoriali

print(fattoriale())
'''
#esercizio 4
'''
def dizionario():
    n : int = int(input("Number please: "))
    numeri : dict = {}
    i:int=0
    while i <= n:
        i+=1
        numeri[i] = i*i
    print(numeri)
dizionario()
'''
#esericizio 5
'''
def separate():
    stringa = "Without, hello, bag, world"
    res = stringa.split(',')
    output_str : str = ''
    res1 = sorted(res)
    print(res1)


    for i in res:
        output_str += i + ','
    print(output_str)
separate()
'''
#FIBONACCI

"""
def fibonacci_for(numero:int) -> int:
    memoria: list = [0,1]
    for i in range(1, numero):
        risultato : int = memoria[i-1] + memoria[i]
        memoria.append(risultato)
    return memoria[-1]
"""
"""
def fibonacci(numero:int = 5) -> int :
    x = 1
    y = 1
    for i in range (1, numero) :
        k = x+y
        y = k+x
        x = k+y
        print(k)
    return k
fibonacci()
"""

def fib(n : int):
    a = 0
    b = 1
    if (n >= 0):
        print(a, end=' ')
    if (n >= 1):
        print(b, end=' ')
    for i in range(2, n+1):
        c = a + b
        print(c, end=' ')
        a = b
        b = c

fib(n = 5)
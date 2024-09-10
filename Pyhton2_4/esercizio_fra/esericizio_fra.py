def A_Ex3(file_path):
    costi_totali = {}
    totale_preventivo = 0.0
    
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            line = line.strip()
            prodotto, importo_unitario, quantita = line.split(';')

            importo_unitario = float(importo_unitario.strip())

            quantita = int(quantita.strip())

            costo_totale = importo_unitario * quantita
            costi_totali[prodotto.strip()] = costo_totale
            totale_preventivo += costo_totale
    
    costo_massimo = max(costi_totali.values())

    prodotti_costo_massimo = {}    
    for prodotto, costo in costi_totali.items():
        if costo == costo_massimo:
            prodotti_costo_massimo[prodotto] = costo
    prodotti_costo_massimo['Totale'] = totale_preventivo

    return prodotti_costo_massimo

result = A_Ex3('preventivo.txt')
print(result)
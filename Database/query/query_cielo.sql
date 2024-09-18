'1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?
2. Quali sono le compagnie che hanno voli che superano le 3 ore?
3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con
codice ‘CIA’ ?
4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice
‘FCO’ ?
5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’
e arrivano all’aeroporto ‘JFK’ ?'

SELECT Volo.codice, Volo.comp
FROM Volo
WHERE Volo.durataMinuti > 180;

SELECT DISTINCT Volo.comp 
FROM Volo
WHERE Volo.durataMinuti > 180;

SELECT ArrPart.codice, ArrPart.comp 
FROM ArrPart
WHERE ArrPart.partenza = 'CIA';

SELECT DISTINCT ArrPart.comp
FROM ArrPart
WHERE ArrPart.arrivo = 'FCO';

SELECT DISTINCT ArrPart.codice, ArrPart.comp
FROM ArrPart
WHERE ArrPart.partenza = 'FCO' and ArrPart.arrivo = 'JFK'; 

'6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atter-
rano all’aeroporto ‘JFK’ ?
7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla
città di ‘New York’ ?
8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli
della compagnia di nome ‘MagicFly’ ?
9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice
del volo, nome della compagnia, e aeroporti di partenza e arrivo.
10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia,
codici dei voli, e aeroporti di partenza, scalo e arrivo.
11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atter-
rano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?'

SELECT ArrPart.comp
FROM ArrPart
WHERE ArrPart.partenza = 'FCO' and ArrPart.arrivo = 'JFK';

SELECT DISTINCT ArrPart.comp
FROM ArrPart, LuogoAeroporto l1, LuogoAeroporto l2
WHERE l1.aeroporto = ArrPart.partenza AND l2.aeroporto = ArrPart.arrivo 
AND l1.citta = 'Roma' and l2.citta = 'New York';

SELECT DISTINCT Aeroporto.codice, Aeroporto.nome, LuogoAeroporto.citta
FROM Aeroporto, ArrPart, LuogoAeroporto
WHERE LuogoAeroporto.aeroporto = ArrPart.partenza AND Aeroporto.codice = ArrPart.partenza 
AND ArrPart.comp = 'MagicFly';

SELECT Volo.codice, Volo.comp, ArrPart.arrivo, ArrPart.partenza<\ 
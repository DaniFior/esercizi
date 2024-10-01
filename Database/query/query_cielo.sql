'1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?'
SELECT Volo.codice, Volo.comp
FROM Volo
WHERE Volo.durataMinuti > 180;

'2. Quali sono le compagnie che hanno voli che superano le 3 ore?'
SELECT DISTINCT Volo.comp 
FROM Volo
WHERE Volo.durataMinuti > 180;

'3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con
codice ‘CIA’ ?'
SELECT ArrPart.codice, ArrPart.comp 
FROM ArrPart
WHERE ArrPart.partenza = 'CIA';

'4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice
‘FCO’ ?'
SELECT DISTINCT ArrPart.comp
FROM ArrPart
WHERE ArrPart.arrivo = 'FCO';

'5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’
e arrivano all’aeroporto ‘JFK’ ?'
SELECT DISTINCT ArrPart.codice, ArrPart.comp
FROM ArrPart
WHERE ArrPart.partenza = 'FCO' and ArrPart.arrivo = 'JFK'; 

'6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atter-
rano all’aeroporto ‘JFK’ ?'

SELECT ArrPart.comp
FROM ArrPart
WHERE ArrPart.partenza = 'FCO' and ArrPart.arrivo = 'JFK';

'7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla
città di ‘New York’ ?'
SELECT DISTINCT ArrPart.comp
FROM ArrPart, LuogoAeroporto l1, LuogoAeroporto l2
WHERE l1.aeroporto = ArrPart.partenza AND l2.aeroporto = ArrPart.arrivo 
AND l1.citta = 'Roma' and l2.citta = 'New York';

'8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli
della compagnia di nome ‘MagicFly’ ?'
SELECT DISTINCT Aeroporto.codice, Aeroporto.nome, LuogoAeroporto.citta
FROM Aeroporto, ArrPart, LuogoAeroporto
WHERE LuogoAeroporto.aeroporto = ArrPart.partenza AND Aeroporto.codice = ArrPart.partenza 
AND ArrPart.comp = 'MagicFly';

'9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice
del volo, nome della compagnia, e aeroporti di partenza e arrivo.'
SELECT V.codice, V.comp, AP.partenza, AP.arrivo
FROM Volo V
JOIN ArrPart AP ON V.codice = AP.codice AND V.comp = AP.comp
JOIN LuogoAeroporto LA1 ON AP.partenza = LA1.aeroporto
JOIN LuogoAeroporto LA2 ON AP.arrivo = LA2.aeroporto
WHERE LA1.citta = 'Roma'
AND LA2.citta = 'New York';

'10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia,
codici dei voli, e aeroporti di partenza, scalo e arrivo.'
SELECT V1.comp, V1.codice AS volo_1, V2.codice AS volo_2, AP1.partenza AS aeroporto_partenza, AP1.arrivo AS aeroporto_scalo, AP2.arrivo AS aeroporto_arrivo
FROM Volo V1
JOIN ArrPart AP1 ON V1.codice = AP1.codice AND V1.comp = AP1.comp
JOIN Volo V2 ON V1.comp = V2.comp
JOIN ArrPart AP2 ON V2.codice = AP2.codice AND V2.comp = AP2.comp
JOIN LuogoAeroporto LA1 ON AP1.partenza = LA1.aeroporto
JOIN LuogoAeroporto LA2 ON AP2.arrivo = LA2.aeroporto
JOIN LuogoAeroporto LAS ON AP1.arrivo = LAS.aeroporto AND AP2.partenza = LAS.aeroporto
WHERE LA1.citta = 'Roma'
AND LA2.citta = 'New York'
AND AP1.arrivo = AP2.partenza;

'11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atter-
rano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?'
SELECT C.nome
FROM Compagnia C
JOIN Volo V ON C.nome = V.comp
JOIN ArrPart AP ON V.codice = AP.codice AND V.comp = AP.comp
WHERE AP.partenza = 'FCO'
AND AP.arrivo = 'JFK'
AND C.annoFondaz IS NOT NULL;

'1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi
aeroporti?'
SELECT Aeroporto.codice, Aeroporto.nome, COUNT(DISTINCT comp) 
FROM Aeroporto, ArrPart
WHERE ArrPart.partenza = Aeroporto.codice
OR ArrPart.arrivo = Aeroporto.codice
GROUP BY Aeroporto.codice, Aeroporto.nome;

'2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno
100 minuti?'
SELECT COUNT(*) AS num_voli
FROM ArrPart, Volo
WHERE ArrPart.partenza = 'HTR'
AND Volo.codice = ArrPart.codice
AND Volo.durataminuti >= 100;

'3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione
nella quale opera?'
SELECT LuogoAeroporto.nazione, COUNT(DISTINCT aeroporto) AS num_aeroporti
FROM ArrPart, Aeroporto, LuogoAeroporto
WHERE 
    (ArrPart.partenza = LuogoAeroporto.aeroporto OR ArrPart.arrivo = LuogoAeroporto.aeroporto)
    AND ArrPart.comp = 'Apitalia'
GROUP BY LuogoAeroporto.nazione;

'4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla
compagnia ‘MagicFly’?'
SELECT AVG(Volo.durataminuti) AS media, MIN(Volo.durataminuti) AS minimo, max(Volo.durataminuti) AS massimo
FROM Volo
WHERE Volo.comp = 'MagicFly';

'5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli
aeroporti?'
SELECT Aeroporto.codice, Aeroporto.nome, min(Compagnia.annofondaz) AS anno
FROM Compagnia, Aeroporto, ArrPart
WHERE Compagnia.nome = ArrPart.comp
AND (Aeroporto.codice = ArrPart.arrivo OR Aeroporto.codice = ArrPart.partenza)
GROUP BY Aeroporto.codice, Aeroporto.nome;

'6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più
voli?'
SELECT  LuogoAeroporto1.nazione AS nazione, COUNT(DISTINCT LuogoAeroporto2.nazione) AS nazioni_raggiungibili
FROM LuogoAeroporto LuogoAeroporto1, LuogoAeroporto LuogoAeroporto2, ArrPart
WHERE ArrPart.partenza = LuogoAeroporto1.aeroporto
AND ArrPart.arrivo = LuogoAeroporto2.aeroporto
AND LuogoAeroporto1.nazione <> LuogoAeroporto2.nazione
GROUP BY LuogoAeroporto1.nazione;

'7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?'
SELECT Aeroporto.codice, Aeroporto.nome, AVG(Volo.durataminuti) AS media_durata
FROM Volo, ArrPart, Aeroporto 
WHERE Volo.codice = ArrPart.codice
AND Volo.comp = ArrPart.comp
AND Aeroporto.codice = ArrPart.partenza
GROUP BY Aeroporto.codice, Aeroporto.nome;

'8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate
a partire dal 1950?'
SELECT Compagnia.nome, sum(Volo.durataminuti) AS durata_tot
FROM Volo, Compagnia
WHERE Compagnia.annofondaz >= 1950
AND Compagnia.nome = Volo.comp
GROUP BY Compagnia.nome;

'9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?'
SELECT Aeroporto.codice, Aeroporto.nome
FROM  Aeroporto, ArrPart
WHERE (Aeroporto.codice = ArrPart.arrivo OR Aeroporto.codice = ArrPart.partenza)
GROUP BY Aeroporto.codice
HAVING COUNT(DISTINCT ArrPart.comp) = 2;

'10. Quali sono le città con almeno due aeroporti?'
SELECT LuogoAeroporto.citta
FROM  LuogoAeroporto
GROUP BY LuogoAeroporto.citta
HAVING COUNT(DISTINCT LuogoAeroporto.aeroporto) >= 2;

'11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6
ore?'
SELECT Volo.comp AS compagnia
FROM Volo
GROUP BY Volo.comp
HAVING AVG(Volo.durataminuti) > 360;

'12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100
minuti?'
SELECT Volo.comp AS compagnia
FROM Volo
GROUP BY Volo.comp
HAVING min(Volo.durataminuti) > 100;
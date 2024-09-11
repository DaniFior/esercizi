SELECT Persona.cognome
FROM Persona
WHERE posizione = Strutturato 

SELECT Persona.nome, Persona.cognome
FROM Persona
WHERE posizione = ricercatore

SELECT Persona.cognome
FROM Persona
WHERE posizione = professore_associato 
AND cognome like 'V%'

SELECT cognome
FROM Persona
WHERE posizione = professore_associato
AND posizione = professore_ordinario
AND cognome like 'V%'

SELECT Progetto.id
FROM Progetto
WHERE fine < date

SELECT Progetto.nome
FROM Progetto
ORDER BY date

SELECT WP.nome
FROM WP
ORDER BY nome

SELECT DISTINCT Assenza.tipo
FROM Assenza

SELECT DISTINCT AttivitaProgetto.tipologia
FROM AttivitaProgetto

SELECT DISTINCT AttivitaNonProgettuale.giorno
FROM AttivitaNonProgettuale
WHERE tipo = 'didattica'
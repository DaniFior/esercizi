SELECT Persona.cognome
FROM Persona;

SELECT Persona.*
FROM Persona
WHERE Persona.posizione = 'Ricercatore';

SELECT Persona.*
FROM Persona
WHERE Persona.posizione = 'Professore Associato' AND Persona.cognome like 'V%';

SELECT cognome
FROM Persona
WHERE (Persona.posizione = 'Professore Associato' OR posizione = 'Professore Ordinario')
AND cognome like 'V%';

SELECT Progetto.*
FROM Progetto
WHERE Progetto.fine < current_date;

SELECT Progetto.*
FROM Progetto
ORDER BY Progetto.inizio;

SELECT WP.*
FROM WP
ORDER BY WP.nome;

SELECT DISTINCT Assenza.tipo
FROM Assenza;

SELECT DISTINCT AttivitaProgetto.tipo
FROM AttivitaProgetto;

SELECT DISTINCT AttivitaNonProgettuale.giorno
FROM AttivitaNonProgettuale
WHERE AttivitaNonProgettuale.tipo = 'Didattica';
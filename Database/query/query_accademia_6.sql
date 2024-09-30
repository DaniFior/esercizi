'1. Quanti sono gli strutturati di ogni fascia?'
SELECT Persona.posizione, COUNT(*) AS numero_strutturati
FROM Persona
GROUP BY posizione;

'2. Quanti sono gli strutturati con stipendio ≥ 40000?'
SELECT Persona.posizione, COUNT (*) AS numero_strutturati, Persona.stipendio
FROM Persona
WHERE Persona.stipendio > 45000
GROUP BY posizione, stipendio;

'3. Quanti sono i progetti già finiti che superano il budget di 50000?'
SELECT COUNT(*) AS numero_progetti_finiti
FROM Progetto
WHERE fine < CURRENT_DATE AND budget > 50000;

'4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto
‘Pegasus’ ?'
SELECT AVG(oreDurata) AS media_ore, MAX(oreDurata) AS massimo_ore, MIN(oreDurata) AS minimo_ore
FROM AttivitaProgetto
JOIN Progetto ON AttivitaProgetto.progetto = Progetto.id
WHERE Progetto.nome = 'Pegasus';

'5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
‘Pegasus’ da ogni singolo docente?'
SELECT Persona.nome, Persona.cognome, AVG(oreDurata) AS media_ore, MAX(oreDurata) AS massimo_ore, MIN(oreDurata) AS minimo_ore
FROM AttivitaProgetto
JOIN Progetto ON AttivitaProgetto.progetto = Progetto.id
JOIN Persona ON AttivitaProgetto.persona = Persona.id
WHERE Progetto.nome = 'Pegasus'
GROUP BY Persona.id, Persona.nome, Persona.cognome;

'6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?'
SELECT Persona.nome, Persona.cognome, SUM(oreDurata) AS totale_ora
FROM AttivitaNonProgettuale
JOIN Persona ON AttivitaNonProgettuale.persona = Persona.id
WHERE tipo = 'Didattica'
GROUP BY Persona.nome, Persona.cognome;

'7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?'
SELECT AVG(stipendio) as media, MAX(stipendio) AS massimo, MIN(stipendio) AS minimo
FROM Persona
WHERE Persona.posizione = 'Ricercatore';

'8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori
associati e dei professori ordinari?'
SELECT AVG(stipendio) as media, MAX(stipendio) AS massimo, MIN(stipendio) AS minimo
FROM Persona
WHERE posizione IN ('Ricercatore', 'Professore Ordinario', 'Professore Associato')
GROUP BY posizione;

'9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?'
SELECT Progetto.nome AS nome_progetto, SUM(AttivitaProgetto.oreDurata) AS totale_ore
FROM AttivitaProgetto
JOIN Persona ON AttivitaProgetto.persona = Persona.id
JOIN Progetto ON AttivitaProgetto.progetto = Progetto.id
WHERE Persona.nome = 'Ginevra' AND Persona.cognome = 'Riva'
GROUP BY Progetto.nome;

'10. Qual è il nome dei progetti su cui lavorano più di due strutturati?'
SELECT Progetto.id, Progetto.nome
FROM AttivitaProgetto, Progetto
WHERE Progetto.id = AttivitaProgetto.progetto
GROUP BY Progetto.id, Progetto.nome
HAVING COUNT(AttivitaProgetto.tipo)>2;

'11. Quali sono i professori associati che hanno lavorato su più di un progetto?'
SELECT Persona.nome, Persona.cognome
FROM AttivitaProgetto
JOIN Persona ON AttivitaProgetto.persona = Persona.id
WHERE Persona.posizione = 'Professore Associato'
GROUP BY Persona.id, Persona.nome, Persona.cognome
HAVING COUNT(DISTINCT AttivitaProgetto.progetto) > 1;
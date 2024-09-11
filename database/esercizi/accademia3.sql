CREATE DATABASE Accademia;

CREATE TYPE Strutturato AS ENUM ('ricercatore', 'professore_associato', 'professore_ordinario');
CREATE TYPE LavoroProgetto AS ENUM ('ricerca_sviluppo', 'dimostrazione', 'management', 'altro');
CREATE TYPE LavoroNonProgettuale AS ENUM ('didattica', 'ricerca', 'missione', 'incontro_dipartimentale', 'incontro_accademico', 'altro');
CREATE TYPE CausaAssenza AS ENUM ('chiusura_universitaria', 'maternita', 'malattia');

CREATE DOMAIN PosInteger AS integer
    check (value >= 0);
CREATE DOMAIN StringaM as varchar(100);
CREATE DOMAIN NumeroOre as integer
    check (value >= 0 and value <= 8);
CREATE DOMAIN Denaro as float
    check (value >= 0);

CREATE TABLE Persona (
    id PosInteger not null,
    nome StringaM not null,
    cognome StringaM not null,
    posizione Strutturato not null, 
    stipendio Denaro not null, 
    PRIMARY KEY(id)
);

CREATE TABLE Progetto (
    id PosInteger not null, 
    nome StringaM not null, 
    inizio date not null, 
    fine date not null check (inizio<fine), 
    budget Denaro not null, 
    PRIMARY KEY(id),
    unique(nome)
);

CREATE TABLE WP (
    progetto PosInteger not null,
    id PosInteger not null,
    nome StringaM not null, 
    inizio date not null,
    fine date not null check (inizio<fine),
    unique(progetto, nome),
    PRIMARY KEY(progetto, id),
    FOREIGN KEY(progetto) REFERENCES Progetto(id)
);

CREATE TABLE AttivitaProgetto (
    id PosInteger not null,
    persona PosInteger not null, 
    progetto PosInteger not null,
    wp PosInteger not null, 
    giorno date not null,
    tipo LavoroProgetto not null, 
    oreDurata NumeroOre not null,
    FOREIGN KEY (persona) REFERENCES Persona(id),
    FOREIGN KEY (progetto, wp) REFERENCES WP(progetto, id) 
);

CREATE TABLE AttivitaNonProgettuale(
    id PosInteger not null, 
    persona PosInteger not null,
    progetto PosInteger not null, 
    wp PosInteger not null, 
    giorno date not null,
    tipo LavoroProgetto not null, 
    oreDurata NumeroOre not null,
    PRIMARY KEY(id),
    FOREIGN KEY (persona) REFERENCES Persona(id)
);

CREATE TABLE Assenza(
    id PosInteger not null,
    persona PosInteger not null, 
    tipo CausaAssenza not null, 
    giorno date not null,
    PRIMARY KEY(id),
    unique(persona, giorno),
    FOREIGN KEY (persona) REFERENCES Persona(id)
);  
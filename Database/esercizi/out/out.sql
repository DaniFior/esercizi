CREATE DATABASE OUT;

CREATE DOMAIN Valuta AS 
char(3) (check value is not null)

CREATE DOMAIN Importo AS NUMERIC(10, 3) 
(check value is not null)

CREATE TYPE Denaro as (
    valuta Valuta,
    importo Importo
);

CREATE TABLE Nazione (
    Nome varchar not null,
    PRIMARY KEY(Nome)
);

CREATE TABLE Regione (
    nome varchar not null,
    nazione varchar not null,
    PRIMARY KEY (nome, nazione),
    FOREIGN KEY nazione REFERENCES Nazione(nome)
);

CREATE TABLE Citta (
    nome varchar not null,
    regione varchar not null,
    nazione varchar not null,
    PRIMARY KEY(nome, regione, nazione),
    FOREIGN KEY(regione, nazione) REFERENCES Regione(nome, nazione)
);

CREATE TABLE Sede(
    id serial primary key not null,
    nome varchar not null,
    indirizzo Indirizzo not null,
    citta varchar not null,
    regione varchar not null,
    nazione varchar not null,
    FOREIGN KEY (citta, regione, nazione)
        REFERENCES citta(nome, regione, nazione)
);

CREATE TABLE Sala (
    nome varchar not null,
    sede integer not null,
    PRIMARY KEY(nome, sede),
    FOREIGN KEY (sede) 
        REFERENCES Sede(id)
);

CREATE TABLE Settore (
    id serial primary key not null,
    nome varchar not null,
    sala varchar not null,
    sede integer not null,
    UNIQUE (nome, sala, sede),
    FOREIGN KEY(sala, sede)
        REFERENCES Sala(nome, sede) 
);

CREATE TABLE Posto(
    fila Integer not null,
    colonna Integer not null,  
    settore integer not null,
    FOREIGN KEY (settore) REFERENCES Settore(id),
    PRIMARY KEY(fila, colonna, settore) 
);

CREATE TABLE Artista(
    id serial integer not null,
    nome varchar not null,
    cognome varchar not null,
    nome_arte varchar,
    PRIMARY KEY(id)
);

CREATE TABLE TipologiaSpettacolo(
    nome varchar not null,
    PRIMARY KEY(nome)
);  

CREATE TABLE Genere (
    nome varchar not null,
    PRIMARY KEY(nome)
);

CREATE TABLE Spettacolo (
    id serial integer not null,
    nome varchar not null,
    durata_min integer not null,
    tipologiaspettacolo varchar not null,
    genere varchar not null,
    PRIMARY KEY(id),
    FOREIGN KEY (tipologiaspettacolo)
        REFERENCES TipologiaSpettacolo(nome)
    FOREIGN KEY (genere)
        REFERENCES Genere(nome)
    -- v.incl id ccorre in Partecipa(spettacolo)
);

CREATE TABLE Spettacolo_Artista (
    spettacolo varchar not null,
    artista integer not null,
    PRIMARY KEY (spettacolo, artista),
    FOREIGN KEY (spettacolo)
        REFERENCES Spettacolo(nome),
    PRIMARY KEY (artista)
        REFERENCES Artista(id)
);

CREATE TABLE Evento (
    id serial integer not null,
    data Date not null,
    orario Time not null,
    spettacolo integer not null,
    sala varchar not null,
    sede varchar not null,
    PRIMARY KEY(id),
    FOREIGN KEY (spettacolo)
        REFERENCES Spettacolo(id)
    FOREIGN KEY(sala, sede)
        REFERENCES Sala(nome, sede)
);

CREATE TABLE TipoTariffa(
    nome varchar not null,
    PRIMARY KEY(nome)
);

CREATE TABLE Tariffa (
    prezzo Denaro not null,
    tipotariffa varchar not null,
    settore integer not null,
    evento integer not null,
    PRIMARY KEY(tipotariffa, settore, evento),
    FOREIGN KEY (tipotariffa)
        REFERENCES TipoTariffa(nome),
    FOREIGN KEY (settore)
        REFERENCES Settore(id),
    FOREIGN KEY(evento)
        REFERENCES Evento(id)
);

CREATE TABLE Prenotazione(
    id integer not null,
    evento integer not null,
    utente varchar not null, 
    PRIMARY KEY(id)
    FOREIGN KEY (evento, spettacolo, sala, sede)
        REFERENCES Evento(id, spettacolo, sala, sede),
    FOREIGN KEY utente 
        REFERENCES Utente(cf)
);

CREATE TABLE pre_posto (
    prenotazione integer not null,
    tipotariffa varchar not null,
    fila integer not null,
    colonna integer not null,
    settore integer not null,
    PRIMARY KEY(prenotazione, fila, colonna),
    FOREIGN KEY (prenotazione) REFERENCES Prenotazione(id),
    FOREIGN KEY (tipotariffa) REFERENCES TipoTariffa(nome),
    FOREIGN KEY (fila, colonna, settore) REFERENCES Posto(fila, colonna, settore)
);

CREATE TABLE Utente(
    cf varchar not null,
    nome varchar not null,
    cognome varchar not null,
    PRIMARY KEY(cf)
);
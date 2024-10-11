CREATE DOMAIN StringNotNull AS VARCHAR
    check (VALUE is not null);

CREATE DOMAIN Civico AS VARCHAR 
    check (VALUE ~ '[0-9]+(/[a-z]+)?');

CREATE DOMAIN CAP AS VARCHAR    
    check (VALUE ~ '[0-9]{5}' and VALUE is not null);

CREATE TYPE Indirizzo (
    via StringNotNull,
    civico Civico,
    cap CAP
)

CREATE TABLE Nazione (
    nome VARCHAR, 
    PRIMARY KEY(nome)
);

CREATE TABLE Regione (
    nome VARCHAR,
    PRIMARY KEY(nome)
)

CREATE TABLE reg_naz(
    regione integer not null,
    nazione integer not null,
    FOREIGN KEY(regione) REFERENCES Regione(nome),
    FOREIGN KEY(nazione) REFERENCES Nazione(Nome),
    PRIMARY KEY(regione)
);


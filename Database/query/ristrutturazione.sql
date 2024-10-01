CREATE DOMAIN IN Stringa AS VARCHAR(100):
CHECKS value IS NOT NULL;

CREATE DOMAIN IN Targa AS CHAR(7):
CHECK value ~'^[A-Z]{2}[0-9]{3}[A-Z]{2}$'
AND value IS NOT NULL;

CREATE DOMAIN cap_domain AS VARCHAR(5)
CHECK (value~'^[0-9]{5}$');

CREATE TYPE Indirizzo AS (
via VARCHAR (100),
civico VARCHAR(10),
cap cap_domain
);

CREATE DOMAIN Telefono AS VARCHAR(15)
CHECK (value~'\+?[0-9]{5}$');

CREATE DOMAIN CodiceFiscale AS VARCHAR(16)
CHECK (value~'\+?[A-Z0-9]{16}$');


CREATE TABLE Nazione {
    nome varchar not null
    PRIMARY KEY(nome)
};

CREATE TABLE Regione {
    nome varchar not null,
    nazione varchar not null,
    PRIMARY KEY(nome)
    FOREIGN KEY(nazione) REFERENCES Nazione(nome)
};

CREATE TABLE Citta {
    nome varchar not null, 
    regione varchar not null,
    nazione varchar not null,
    PRIMARY KEY (nome, regione, nazione),
    FOREIGN KEY (regione, nazione) REFERENCES Regione(nome, nazione)
};

CREATE TABLE Riparazione {
    riconsegna timestamp,
    codice int not null,
    inizio timestamp,
    officina varchar not null,
    PRIMARY KEY(codice),
    FOREIGN KEY(officina) REFERENCES Officina(id),
    FOREIGN KEY(veicolo) REFERENCES Veicolo(targa)
};

CREATE TABLE Officina {
    nome varchar not null,
    indirizzo Indirizzo not null,
    id int not null,
    riparazione int not null,
    citta varchar not null, 
    regione varchar not null,
    nazione varchar not null,
    PRIMARY KEY(id),
    FOREIGN KEY(riparazione) REFERENCES Riparazione(codice),
    FOREIGN KEY(citta, regione, nazione) REFERENCES Citta(nome, regione, nazione)
};

CREATE TABLE Marca {
    nome varchar not null, 
    PRIMARY KEY(nome)
};

CREATE TABLE TipoVeicolo {
    nome varchar not null, 
    PRIMARY KEY(nome)
};

CREATE TABLE Modello {
    nome varchar not null,
    marca varchar not null,
    tipoveicolo varchar not null,
    PRIMARY KEY(nome, marca, tipoveicolo),
    FOREIGN KEY(marca) REFERENCES Marca(nome)
    FOREIGN KEY(tipoveicolo) REFERENCES TipoVeicolo(nome)
};

CREATE TABLE Veicolo {
    targa Targa not null,
    immatricolazione int not null,
    marca varchar not null, 
    modello varchar not null, 
    cliente CodiceFiscale not null,
    PRIMARY KEY(targa),
    FOREIGN KEY(marca, modello) REFERENCES Modello(nome, marca)
};

CREATE TABLE Cliente {
    persona CodiceFiscale not null,
    PRIMARY KEY(persona),
    FOREIGN KEY(persona) REFERENCES Persona(cf)
    v.incl.persona occorre in Veicolo(cliente)
};

CREATE TABLE Persona {
    cf CodiceFiscale not null,
    nome varchar not null,
    indirizzo Indirizzo not null,
    telefono varchar not null,
    citta varchar not null,
    PRIMARY KEY(cf),
    FOREIGN KEY(citta) REFERENCES Citta(nome),
};

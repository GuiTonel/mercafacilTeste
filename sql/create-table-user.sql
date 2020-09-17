CREATE table IF NOT EXISTS usuario (
	id serial PRIMARY KEY,
	nome VARCHAR ( 200 ) NOT NULL,
	senha VARCHAR ( 200 ) NOT NULL
);  

DROP TABLE planos;
DROP TABLE alunos;
DROP TABLE treinos;
DROP TABLE instrutores;
DROP TABLE plano_aluno;

CREATE TABLE planos(
	id_plano SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	descricao TEXT NOT NULL,
	tipo VARCHAR(255) NOT NULL,
	preco NUMERIC(10,2) NOT NULL
	-- preco NUMERIC(10,2) NOT NULL CHECK (preco >= 0)
);

SELECT * FROM planos;

CREATE TABLE alunos(
	id_aluno SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	altura NUMERIC(2,2) NOT NULL,
	peso NUMERIC(2,2) NOT NULL,
	data_nascimento VARCHAR(255) NOT NULL,
	senha BYTEA NOT NULL
);

SELECT * FROM alunos;

CREATE TABLE instrutores(
	id_instrutor SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	cpf CHAR(14) NOT NULL,
	senha BYTEA NOT NULL
);

SELECT * FROM instrutores;

CREATE TABLE treinos(
	id_treino SERIAL PRIMARY KEY,
	tipo VARCHAR(255) NOT NULL,
	nome_exercicio VARCHAR(255) NOT NULL,
	peso INT NOT NULL,
	repeticoes INT NOT NULL,
	series INT NOT NULL,
	tempo_descanso VARCHAR(255) NOT NULL,
	id_aluno INTEGER NOT NULL,
	id_instrutor INTEGER NOT NULL,
	FOREIGN KEY (id_aluno) REFERENCES alunos (id_aluno),
	FOREIGN KEY (id_instrutor) REFERENCES instrutores (id_instrutor)
);

SELECT * FROM treinos ORDER BY id_treino;

CREATE TABLE plano_aluno(
	id_plano INTEGER NOT NULL,
	id_aluno INTEGER NOT NULL,
	metodo_pagamento VARCHAR(255) NOT NULL,
	data_hora TIMESTAMP NOT NULL,
	PRIMARY KEY (id_plano, id_aluno),
	FOREIGN KEY (id_plano) REFERENCES planos (id_plano),
	FOREIGN KEY (id_aluno) REFERENCES alunos (id_aluno)
);

SELECT * FROM plano_aluno;

SELECT a.nome, p.nome, pa.metodo_pagamento, pa.data_hora FROM plano_aluno pa 
JOIN planos p ON p.id_plano = pa.id_plano 
JOIN alunos a ON a.id_aluno = pa.id_aluno 
JOIN plano_aluno ON pa.data_hora = pa.data_hora AND pa.metodo_pagamento = pa.metodo_pagamento;

SELECT p.nome, p.descricao, p.tipo, p.preco FROM plano_aluno pa JOIN planos p ON p.id_plano = pa.id_plano WHERE id_aluno = 1;
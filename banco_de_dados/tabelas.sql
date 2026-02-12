DROP TABLE planos;
DROP TABLE alunos;
DROP TABLE treinos;
DROP TABLE instrutores;
DROP TABLE exercicios;
DROP TABLE plano_aluno;
DROP TABLE treino_exercicio;

CREATE TABLE planos(
	id_plano SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	descricao TEXT NOT NULL,
	tipo VARCHAR(255) NOT NULL,
	preco NUMERIC(10,2) NOT NULL
	-- preco NUMERIC(10,2) NOT NULL CHECK (preco >= 0)
);

SELECT * FROM planos ORDER BY id_plano;

CREATE TABLE alunos(
	id_aluno SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	altura NUMERIC(10,2) NOT NULL,
	peso NUMERIC(10,2) NOT NULL,
	data_nascimento VARCHAR(255) NOT NULL,
	senha BYTEA NOT NULL
);

SELECT * FROM alunos ORDER BY id_aluno ASC;

CREATE TABLE instrutores(
	id_instrutor SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	cpf CHAR(14) NOT NULL UNIQUE,
	senha BYTEA NOT NULL
);

SELECT * FROM instrutores ORDER BY id_instrutor ASC;

CREATE TABLE treinos(
	id_treino SERIAL PRIMARY KEY,
	tipo VARCHAR(255) NOT NULL,
	id_aluno INTEGER NOT NULL,
	id_instrutor INTEGER NOT NULL,
	FOREIGN KEY(id_aluno) REFERENCES alunos(id_aluno),
	FOREIGN KEY(id_instrutor) REFERENCES instrutores(id_instrutor)
);

SELECT * FROM treinos ORDER BY id_treino ASC;

CREATE TABLE exercicios(
	id_exercicio SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	quantidade_series INT NOT NULL,
	numero_repeticoes INT NOT NULL,
	peso INT NOT NULL,
	tempo_descanso VARCHAR(255) NOT NULL
);

SELECT * FROM exercicios ORDER BY id_exercicio ASC;

---

CREATE TABLE plano_aluno(
	id_plano INTEGER NOT NULL,
	id_aluno INTEGER NOT NULL,
	metodo_pagamento VARCHAR(255) NOT NULL,
	data_hora TIMESTAMP NOT NULL,
	PRIMARY KEY(id_plano, id_aluno),
	FOREIGN KEY(id_plano) REFERENCES planos(id_plano),
	FOREIGN KEY(id_aluno) REFERENCES alunos(id_aluno)
);

CREATE TABLE treino_exercicio(
	id_treino INTEGER NOT NULL,
	id_exercicio INTEGER NOT NULL,
	PRIMARY KEY(id_treino, id_exercicio),
	FOREIGN KEY(id_treino) REFERENCES treinos(id_treino).
	FOREIGN KEY(id_exercicio) REFERENCES exercicios(id_exercicio).
);

SELECT * FROM plano_aluno ORDER BY id_plano ASC;

---

SELECT a.nome, a.email, p.nome, pa.data_hora, pa.metodo_pagamento FROM plano_aluno pa 
JOIN planos p ON p.id_plano = pa.id_plano 
JOIN alunos a ON a.id_aluno = pa.id_aluno 
JOIN plano_aluno ON pa.data_hora = pa.data_hora AND pa.metodo_pagamento = pa.metodo_pagamento
ORDER BY a.id_aluno ASC;

SELECT p.nome, p.descricao, p.tipo, p.preco FROM plano_aluno pa 
JOIN planos p ON p.id_plano = pa.id_plano WHERE id_aluno = 1;

SELECT a.nome, a.email, a.altura, a.peso FROM treinos t 
JOIN alunos a ON a.id_aluno = t.id_aluno WHERE id_instrutor = 1;

SELECT t.tipo, t.nome_exercicio, t.peso, t.repeticoes, t.series, t.tempo_descanso, i.nome FROM treinos t
JOIN instrutores i ON i.id_instrutor= t.id_instrutor 
ORDER BY t.id_treino ASC; 

SELECT senha FROM alunos WHERE id_aluno = 1;
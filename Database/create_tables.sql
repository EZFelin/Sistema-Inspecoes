CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    setor VARCHAR(100),
    contato VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(100)
);
CREATE TABLE equipamentos (
    id_equipamento SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    setor VARCHAR(100),
    descricao TEXT
);
CREATE TABLE inspecoes (
    id_inspecao SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id_usuario),
    equipamento_id INTEGER REFERENCES equipamentos(id_equipamento),
    data_inspecao DATE,
    status VARCHAR(20),
    observacao TEXT
);
/*Cria a database BIGBIKE caso não exista e seta o charset para UTF8*/
create database if not exists catalogo_jogos character set utf8mb4 collate utf8mb4_0900_ai_ci;

/*Usa a database BIGBIKE*/
use catalogo_jogos;

CREATE TABLE if not exists jogos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(255) NOT NULL,
  descricao TEXT NOT NULL,
  data_lancamento DATE NOT NULL,
  generos VARCHAR(255) NOT NULL,
  desenvolvedora VARCHAR(255) NOT NULL
);
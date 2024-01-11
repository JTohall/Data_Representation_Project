
CREATE DATABASE IF NOT EXISTS movies;

USE movies;

CREATE TABLE movies (id int NOT NULL AUTO_INCREMENT, Movie VARCHAR(250), Rating VARCHAR(20), year int, PRIMARY KEY (id);

INSERT INTO products (id, Movie, Rating, Year) VALUES
('Moana', 'PG', 2016), 
('Encanto', 'PG', 2021), 
('Wish', 'PG', 2023), 
('Little Mermaid', 'G', 1989), 
('Luca', 'PG', 2021), 
('Brave', 'PG', 2012), 
('Elemental', 'PG', 2023), 
('Zootopia', 'PG', 2016), 
('Mulan', 'G', 1998),
('Tangled', 'PG', 2010),
('Frozen', 'PG', 2013), ('Sleeping Beauty', 'G', 1959);
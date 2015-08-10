-- Table definitions for the item catalog project.


DROP DATABASE IF EXISTS catalog;

CREATE DATABASE catalog;

\c catalog;

CREATE TABLE categories ( id SERIAL PRIMARY KEY,
                          name TEXT);
                        
CREATE TABLE items ( id SERIAL PRIMARY KEY,
                     title TEXT,
                     category_id INTEGER REFERENCES categories(id),
                     added_date TIMESTAMP,
                     price NUMERIC,
                     description TEXT);

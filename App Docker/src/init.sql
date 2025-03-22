CREATE TABLE messages (
    id INT  PRIMARY KEY,
    message VARCHAR(255) NOT NULL
);

INSERT INTO messages (message) VALUES ('Hola desde MySQL con FastAPI!');


SELECT * FROM messages;

INSERT INTO messages (id,message) VALUES (1,'Hola desde MySQL con FastAPI!')
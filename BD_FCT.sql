CREATE DATABASE BD_FCT;

USE BD_FCT;

CREATE TABLE IF NOT EXISTS CERVEZAS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    PAIS_ORIGEN VARCHAR(100),
    CATEGORIA VARCHAR(100),
    GRADUACION FLOAT,
    PRECIO DECIMAL(10, 2)
);



INSERT INTO CERVEZAS VALUES 
(1,'Alemania', 'Pilsner', 5.0, 2.50),
(2,'Bélgica', 'Tripel', 8.5, 3.75)
(3, 'España', 'Rubia', 3.5, 2.75),
(4,'Francia', 'Tostada', 5.5, 4.75),
(7, 'Reino Unido', 'Porter', 5.8, 6.50),
(8, 'Países Bajos', 'Blanca', 4.7, 4.25),
(9, 'República Checa', 'Pilsner', 4.0, 3.50),
(10, 'Brasil', 'Lager', 4.3, 2.90),
(11, 'Argentina', 'Roja', 5.2, 4.10),
(12, 'Australia', 'Stout', 6.3, 7.20),
(13, 'Canadá', 'IPA', 6.5, 5.75),
(14, 'Japón', 'Ale', 5.6, 6.90),
(15, 'Suecia', 'Tostada', 4.9, 5.40),
(16, 'Noruega', 'Porter', 7.0, 7.80),
(17, 'Dinamarca', 'Blanca', 5.0, 4.65),
(18, 'Suiza', 'Lager', 4.1, 6.10);


```


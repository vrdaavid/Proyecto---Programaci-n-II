CREATE SCHEMA PROYECTOPROGRAMACIONII;

USE PROYECTOPROGRAMACIONII;

CREATE TABLE Usuarios (NombreUsuario varchar(255), NombreCompleto varchar(255), Clave varchar(255) , PRIMARY KEY(NombreUsuario)) ;

INSERT INTO Usuarios (NombreUsuario, NombreCompleto, Clave) values ("Admin", "Admin", "1234");

SELECT *  FROM Usuarios



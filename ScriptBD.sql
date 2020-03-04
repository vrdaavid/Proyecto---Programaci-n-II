CREATE SCHEMA PROYECTOPROGRAMACIONII;

USE PROYECTOPROGRAMACIONII;

DROP TABLE Usuarios;

CREATE TABLE Usuarios 
(NombreUsuario varchar(255), 
NombreCompleto varchar(255), 
Clave varchar(255), 
Rol varchar(255) ,
 PRIMARY KEY(NombreUsuario)) ;

DROP TABLE Miembros;

CREATE TABLE Miembros 
(NombreCompleto varchar(255), 
Cedula varchar(255), 
FechaNacimiento date , 
ID varchar(255), 
Colaboracion int, 
TipoMiembro varchar(255), 
TipoApadrinado varchar(255) ,
PRIMARY KEY(Cedula)) ;

INSERT INTO Usuarios (NombreUsuario, NombreCompleto, Clave, Rol) values ("Admin", "Admin", "1234", "Administrador");
INSERT INTO Miembros values ("David Vargas", "116699999", "1997-03-02", "100012", "12000", "Padrino", "");

SELECT *  FROM Usuarios;
SELECT * FROM Miembros;



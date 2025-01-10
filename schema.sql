CREATE DATABASE deliverys;

use deliverys;

-- TABLA PARA LOS TRABAJADORES

CREATE TABLE trabajador(
	cedula VARCHAR(10) NOT NULL PRIMARY KEY UNIQUE,
	nombre VARCHAR(20) NOT NULL,
	apellido VARCHAR(20) NOT NULL,
	contrasena VARCHAR(30) NOT NULL,
	rol VARCHAR(30) NOT NULL,
	horas INT NOT NULL default 0,
	sueldo INT NOT NULL default 0,
	datos_transferencia VARCHAR(100) NOT NULL UNIQUE,
	estado INT default 0
);

INSERT INTO trabajador (cedula, nombre, apellido, contrasena, rol, horas, sueldo, datos_transferencia, estado) VALUES ('890432987','Gustavo', 'Diaz', 'trabajador' ,'Ingeniero Informatico', 8, 400,  'Mercantil, 0412432809, 74968958',0);
INSERT INTO trabajador (cedula, nombre, apellido, contrasena, rol, horas, sueldo, datos_transferencia, estado) VALUES ('342374923','Antonio', 'Jimenez', 'trabajador' ,'Comerciante', 5, 500, 'Banesco, 0412893482, 38492834',1);
INSERT INTO trabajador (cedula, nombre, apellido, contrasena, rol, horas, sueldo, datos_transferencia, estado) VALUES ('384927422','Maria', 'Guzman', 'trabajador', 'Expositor', 8, 300,  'Exterior, 0414384832, 9384829', 0);
INSERT INTO trabajador (cedula, nombre, apellido, contrasena, rol, horas, sueldo, datos_transferencia, estado) VALUES ('83473283','Eric', 'Stephenson', 'Administrador', 'Expositor', 8, 300,  'Venezuela, 0414384832, 9384829', 0);
INSERT INTO trabajador (cedula, nombre, apellido, contrasena, rol, horas, sueldo, datos_transferencia, estado) VALUES ('34829423','Kyle', 'Mercury', 'Administrador', 'Expositor', 8, 300,  'Mercantil, 0414384832, 9384829', 0);



-- TABLA PARA LOS MENSAJES

CREATE TABLE mensaje(
	fk_administrador VARCHAR (10) NOT NULL, 
	fk_trabajador VARCHAR (10) NOT NULL,
	contenido VARCHAR (300) NOT NULL,
	FOREIGN KEY(fk_administrador) REFERENCES trabajador(cedula),
	FOREIGN KEY(fk_trabajador) REFERENCES trabajador(cedula),
	leido BOOLEAN default 0
);

INSERT INTO mensaje (fk_trabajador, fk_administrador, contenido, leido) VALUES ("890432987","83473283", "Encargate de la cita de las 5:00 PM.", 0);
INSERT INTO mensaje (fk_trabajador, fk_administrador, contenido, leido) VALUES ("342374923","34829423", "Lo veo en la oficina O-29 al mediodia.", 0);
INSERT INTO mensaje (fk_trabajador, fk_administrador, contenido, leido) VALUES ("384927422","34829423", "Buen trabajo, siga asi!", 0);


DROP DATABASE IF EXISTS Hoteland;
CREATE DATABASE Hoteland;
USE Hoteland;


CREATE TABLE Hostal(
	idHostal Serial,
	habitaciones INT NOT NULL,
	entidad VARCHAR(50) CHECK (entidad <> ''),
	municipio VARCHAR(50) CHECK (municipio <> ''),
	colonia VARCHAR(50) CHECK (colonia <> ''),
	calle VARCHAR(50) CHECK(calle <>''),
	numero VARCHAR(10) NOT NULL,
	cp CHAR(5) NOT NULL CHECK (CHAR_LENGTH(cp)=5),
	
	CONSTRAINT PK_HOSTAL PRIMARY KEY (idHostal)
);


CREATE TABLE Habitacion(
	idHabitacion Serial,
	tipo VARCHAR(20) NOT NULL CHECK(tipo <>''),
	camas INT NOT NULL,
	idHostal BIGINT UNSIGNED NOT NULL,
	
	CONSTRAINT PK_HABITACION PRIMARY KEY (idHabitacion),
	CONSTRAINT FK_PERTENECER FOREIGN KEY (idHostal) REFERENCES Hostal(idHostal)
);


CREATE TABLE Usuario(
	idUsuario SERIAL,
	nombre VARCHAR(50) NOT NULL CHECK(nombre <>''),
	apPaterno VARCHAR(50) NOT NULL CHECK(apPaterno <>''),
	apMaterno VARCHAR(50) NOT NULL CHECK(apMaterno <>''),
	correo VARCHAR(200) NOT NULL CHECK(correo <>''),
	hash_contrasena CHAR(64) NOT NULL,
	fechaNacimiento DATE NOT NULL,
	nacionalidad VARCHAR(50),
	idHostal BIGINT UNSIGNED,
	esAdministrador BOOLEAN NOT NULL,
	esEncargado BOOLEAN NOT NULL,
	esHuesped BOOLEAN NOT NULL,
	
	CONSTRAINT PK_USUARIO PRIMARY KEY (idUsuario),
	CONSTRAINT FK_DIRIGIR FOREIGN KEY (idHostal) REFERENCES Hostal(idHostal)
);


CREATE TABLE Reservacion(
	idReserva SERIAL,
	fechaInicio DATE NOT NULL,
	fechaFin DATE NOT NULL,
	idUsuario BIGINT UNSIGNED NOT NULL,
	idHabitacion BIGINT UNSIGNED NOT NULL,
	
	CONSTRAINT PK_RESERVACION PRIMARY KEY (idReserva),
	CONSTRAINT FK_CLIENTE FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario),
	CONSTRAINT FK_HABITACION FOREIGN KEY (idHabitacion) REFERENCES Habitacion(idHabitacion)
);


CREATE TABLE TelefonoUsuario(
	telefono VARCHAR(15) NOT NULL,
	idUsuario BIGINT UNSIGNED NOT NULL,
	
	CONSTRAINT PK_TELEFONO PRIMARY KEY (telefono, idUsuario),
	CONSTRAINT FK_DUENO FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario)
);


CREATE TABLE Actividad(
	idActividad SERIAL,
	titulo VARCHAR(20) NOT NULL CHECK(titulo <>''),
	descripcion VARCHAR(250) NOT NULL CHECK(descripcion <>''),
	imagenPath VARCHAR(256) NOT NULL CHECK(imagenPath <>''),
	precio DECIMAL(6,2) NOT NULL,
	idHostal BIGINT UNSIGNED NOT NULL,
	
	CONSTRAINT PK_ACTIVIDAD PRIMARY KEY (idActividad),
	CONSTRAINT FK_OFRECER FOREIGN KEY (idHostal) REFERENCES Hostal(idHostal)
);


CREATE TABLE Inscripcion(
	idInscripcion Serial,	
	idUsuario BIGINT UNSIGNED NOT NULL,
	idActividad BIGINT UNSIGNED NOT NULL,
	
	CONSTRAINT PK_INSCRIPCION PRIMARY KEY (idInscripcion),
	CONSTRAINT FK_PARTICIPANTE FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario),
	CONSTRAINT FK_ACTIVIDAD FOREIGN KEY (idActividad) REFERENCES Actividad(idActividad)
);

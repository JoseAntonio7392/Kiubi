CREATE TABLE aeropuertos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    ciudad VARCHAR(255) NOT NULL,
    pais VARCHAR(255) NOT NULL,
    codigo VARCHAR(3) NOT NULL,
    codigo_iata CHAR(3),
    codigo_icao CHAR(4)
);

CREATE TABLE vuelos (
    id SERIAL PRIMARY KEY,
    aerolinea VARCHAR(255) NOT NULL,
    aeropuerto_salida_id INT REFERENCES aeropuertos(id),
    aeropuerto_llegada_id INT REFERENCES aeropuertos(id),
    hora_salida TIMESTAMP NOT NULL,
    precio NUMERIC(10,2) NOT NULL,
    moneda VARCHAR(3) NOT NULL,
    duracion INTERVAL NOT NULL,
    asientos_disponibles INT NOT NULL,
    estado VARCHAR(50)
);

INSERT INTO aeropuertos (nombre, ciudad, pais, codigo, codigo_iata) 
VALUES ('Aeropuerto Internacional de la Ciudad de México', 'Ciudad de México', 'México', 'MEX', 'MEX'),
       ('Aeropuerto Internacional de Cancún', 'Cancún', 'México', 'CUN', 'CUN');

INSERT INTO vuelos (aerolinea, aeropuerto_salida_id, aeropuerto_llegada_id, hora_salida, precio, moneda, duracion, asientos_disponibles, estado)
VALUES ('Aeroméxico', 1, 2, '2025-04-15 10:00:00', 300.00, 'USD', '3 hours 45 minutes', 50, 'Programado'),
       ('Volaris', 1, 2, '2025-04-15 12:00:00', 250.00, 'USD', '4 hours 10 minutes', 30, 'Programado');
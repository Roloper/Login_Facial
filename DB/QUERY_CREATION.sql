CREATE TABLE Usuario (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT,
  Nombre VARCHAR(100),
  correo VARCHAR(100),
  contrasena VARCHAR(100),
  admin BOOLEAN DEFAULT FALSE,
  imagen_perfil BLOB DEFAULT NULL,
  imagen_test BLOB DEFAULT NULL
);

CREATE TABLE Venta (
  id_venta INT PRIMARY KEY AUTO_INCREMENT,
  fecha DATE,
  obs VARCHAR(255),
  id_usuario INT,
  FOREIGN KEY (id_usuario) REFERENCES Usuario (id_usuario)
);

CREATE TABLE Producto (
  id_producto INT PRIMARY KEY AUTO_INCREMENT,
  nombre_produc VARCHAR(100),
  descripcion VARCHAR(255),
  precio_uni INT,
  id_usuario INT,
  FOREIGN KEY (id_usuario) REFERENCES Usuario (id_usuario)
);

CREATE TABLE Detalle (
  id_venta INT,
  id_producto INT AUTO_INCREMENT,
  cantidad INT,
  precio_total INT,
  PRIMARY KEY (id_venta, id_producto),
  FOREIGN KEY (id_venta) REFERENCES Venta (id_venta),
  FOREIGN KEY (id_producto) REFERENCES Producto (id_producto)
);
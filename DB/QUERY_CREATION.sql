-- Crear tabla Venta
CREATE TABLE Venta (
  id_venta INT PRIMARY KEY AUTO_INCREMENT,
  fecha INT,
  obs INT,
  id_usuario INT,
  FOREIGN KEY (id_usuario) REFERENCES Vendedor(id_usuario)
);

-- Crear tabla Producto
CREATE TABLE Producto (
  id_producto INT PRIMARY KEY AUTO_INCREMENT,
  nombre_produc INT,
  descripcion INT,
  precio_uni INT,
  id_usuario INT,
  FOREIGN KEY (id_usuario) REFERENCES Vendedor(id_usuario)
);

-- Crear tabla Detalle
CREATE TABLE Detalle (
  id_venta INT,
  id_producto INT,
  cantidad INT,
  precio_total INT,
  PRIMARY KEY (id_venta, id_producto),
  FOREIGN KEY (id_venta) REFERENCES Venta(id_venta),
  FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);

-- Crear tabla Vendedor
CREATE TABLE Vendedor (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT,
  imagen_test INT,
  FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- Crear tabla Admin
CREATE TABLE Admin (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT,
  FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- Crear tabla Usuario
CREATE TABLE Usuario (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT,
  Nombre INT,
  correo INT,
  contraseña INT,
  imagen_perfil INT
);

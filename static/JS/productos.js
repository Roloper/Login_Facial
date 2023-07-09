var admin = true;

function tipodeRol() {
  var rolUser = document.getElementById("rolUser");
  rolUser.textContent = admin ? "Admin" : "Usuario";

  if (!admin) {
    // Desaparecer la opción de vendedores
    var vendedoresOpcion = document.querySelector("a[href='vendedores.html']").parentNode;
    vendedoresOpcion.style.display = "none";

    // Cambiar la referencia de la opción inicio
    var inicioOpcion = document.querySelector("a[href='index.html']");
    inicioOpcion.href = "indexUsuario.html";
  }
}

function llenarTabla() {
  var tabla = document.querySelector('.Cuadro2 table');

  for (var i = 0; i < 10; i++) {
    var fila = document.createElement('tr');

    var idProducto = document.createElement('td');
    idProducto.textContent = generarIDProducto();

    var nombre = document.createElement('td');
    nombre.textContent = generarNombre();

    var descripcion = document.createElement('td');
    descripcion.textContent = generarDescripcion();

    var stock = document.createElement('td');
    stock.textContent = generarStock();

    var precioUnitario = document.createElement('td');
    precioUnitario.textContent = generarPrecioUnitario();

    fila.appendChild(idProducto);
    fila.appendChild(nombre);
    fila.appendChild(descripcion);
    fila.appendChild(stock);
    fila.appendChild(precioUnitario);

    tabla.appendChild(fila);
  }
}

function generarIDProducto() {
  // Generar un ID de producto ficticio
  return Math.floor(Math.random() * 1000) + 1;
}

function generarNombre() {
  // Generar un nombre ficticio para el producto
  var nombres = ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4', 'Producto 5'];
  var indice = Math.floor(Math.random() * nombres.length);
  return nombres[indice];
}

function generarDescripcion() {
  // Generar una descripción ficticia para el producto
  var descripciones = ['Descripción 1', 'Descripción 2', 'Descripción 3', 'Descripción 4', 'Descripción 5'];
  var indice = Math.floor(Math.random() * descripciones.length);
  return descripciones[indice];
}

function generarStock() {
  // Generar una cantidad de stock ficticia
  return Math.floor(Math.random() * 100) + 1;
}

function generarPrecioUnitario() {
  // Generar un precio unitario ficticio
  return '$' + (Math.random() * 100).toFixed(2);
}

llenarTabla();
tipodeRol();

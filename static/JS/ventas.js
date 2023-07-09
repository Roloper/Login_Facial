var admin = true;

function tipodeRol() {
  var rolUser = document.getElementById("rolUser");
  rolUser.textContent = admin ? "Admin" : "Usuario";

  if (!admin) {
    // Desaparecer la opción de vendedores
    var vendedoresOpcion = document.querySelector("a[href='../templates/vendedores.html']").parentNode;
    vendedoresOpcion.style.display = "none";

    // Cambiar la referencia de la opción inicio
    var inicioOpcion = document.querySelector("a[href='../templates/index.html']");
    inicioOpcion.href = "indexUsuario.html";
  }
}

function llenarTabla() {
    var tabla = document.querySelector('.Cuadro2 table');
  
    for (var i = 0; i < 10; i++) {
      var fila = document.createElement('tr');
  
      var fecha = document.createElement('td');
      fecha.textContent = generarFecha();
  
      var vendedor = document.createElement('td');
      vendedor.textContent = generarVendedor();
  
      var observaciones = document.createElement('td');
      observaciones.textContent = generarObservaciones();
  
      var items = document.createElement('td');
      items.textContent = generarItems();
  
      var importe = document.createElement('td');
      importe.textContent = generarImporte();
  
      fila.appendChild(fecha);
      fila.appendChild(vendedor);
      fila.appendChild(observaciones);
      fila.appendChild(items);
      fila.appendChild(importe);
  
      tabla.appendChild(fila);
    }
  }
  
  function generarFecha() {
    // Generar una fecha ficticia (puedes adaptar esto a tus necesidades)
    var fecha = new Date();
    var dia = fecha.getDate();
    var mes = fecha.getMonth() + 1;
    var anio = fecha.getFullYear();
    return dia + '/' + mes + '/' + anio;
  }
  
  function generarVendedor() {
    // Generar un nombre ficticio de vendedor
    var vendedores = ['Juan', 'María', 'Pedro', 'Ana', 'Luis'];
    var indice = Math.floor(Math.random() * vendedores.length);
    return vendedores[indice];
  }
  
  function generarObservaciones() {
    // Generar una observación ficticia
    var observaciones = ['Sin observaciones', 'Cliente habitual', 'Pago pendiente'];
    var indice = Math.floor(Math.random() * observaciones.length);
    return observaciones[indice];
  }
  
  function generarItems() {
    // Generar un número de items ficticio
    return Math.floor(Math.random() * 10) + 1;
  }
  
  function generarImporte() {
    // Generar un importe ficticio
    return '$' + (Math.random() * 100).toFixed(2);
  }
  
  llenarTabla();
  tipodeRol();
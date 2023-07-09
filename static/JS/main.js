
function generarVendedores() {
    var contenedor = document.getElementById("contenedorVendedores");
    var vendedores = ["Vendedor 1", "Vendedor 2", "Vendedor 3", "Vendedor 4", "Vendedor 5","Vendedor 1", "Vendedor 2", "Vendedor 3", "Vendedor 4"];
  
    for (var i = 0; i < vendedores.length; i++) {
      var vendedorDiv = document.createElement("div");
      vendedorDiv.className = "vendedor";
  
      var imagen = document.createElement("img");
      imagen.src = "icon/usuarioEjemplo.svg";
      imagen.alt = "salir";
  
      var nombreVendedor = document.createElement("p");
      nombreVendedor.textContent = vendedores[i];
  
      vendedorDiv.appendChild(imagen);
      vendedorDiv.appendChild(nombreVendedor);
  
      // Verificar si la página actual es "vendedor.html"
      if (window.location.pathname.includes("index1.html")) {
        var correoVendedor = document.createElement("p");
        correoVendedor.textContent = "correo@ejemplo.com";
        correoVendedor.id = "correo"; // Agregar el id "correo"
        vendedorDiv.appendChild(correoVendedor);
      }
  
      contenedor.appendChild(vendedorDiv);
    }
  }
    
    function generarVentas() {
      var ventas = [
        { numeroVenta: "Venta 0145", total: "58.50" },
        { numeroVenta: "Venta 0144", total: "12.60" },
        { numeroVenta: "Venta 0143", total: "124.00" },
        { numeroVenta: "Venta 0142", total: "13.00" },
        { numeroVenta: "Venta 0141", total: "05.80" },
        { numeroVenta: "Venta 0140", total: "21.20" },
        { numeroVenta: "Venta 0139", total: "09.10" },
        { numeroVenta: "Venta 0138", total: "10.00" },
        { numeroVenta: "Venta 0137", total: "10.00" },
        { numeroVenta: "Venta 0136", total: "10.00" },
        { numeroVenta: "Venta 0135", total: "10.00" }
      ];
    
      var tabla = document.getElementById("tablaVentas");
    
      for (var i = 0; i < ventas.length; i++) {
        var fila = document.createElement("tr");
    
        var columnaVenta = document.createElement("td");
        columnaVenta.textContent = ventas[i].numeroVenta;
    
        var columnaTotal = document.createElement("td");
        columnaTotal.textContent = ventas[i].total;
    
        fila.appendChild(columnaVenta);
        fila.appendChild(columnaTotal);
    
        tabla.appendChild(fila);
      }
    }
    
    function generarVendedores1() {
      var contenedor = document.getElementById("contenedorVendedores1");
      var vendedores = ["Vendedor 1", "Vendedor 2", "Vendedor 3", "Vendedor 4", "Vendedor 5"];
    
      for (var i = 0; i < vendedores.length; i++) {
        var vendedorDiv = document.createElement("div");
        vendedorDiv.className = "vendedor1";
    
        var imagen = document.createElement("img");
        imagen.src = "icon/usuarioEjemplo.svg";
        imagen.alt = "salir";
    
        var nombreVendedor = document.createElement("p");
        nombreVendedor.textContent = vendedores[i];
    
        vendedorDiv.appendChild(imagen);
        vendedorDiv.appendChild(nombreVendedor);
    
        contenedor.appendChild(vendedorDiv);
      }
    }
    
    generarVendedores();
    generarVentas();
    
    
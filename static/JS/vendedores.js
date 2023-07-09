var admin = true ;

function tipodeRol(){
  var rolUser = document.getElementById("rolUser");
  rolUser.textContent = admin ? "Admin" : "Usuario";
}

function generarVendedores() {
  var contenedor = document.getElementById("contenedorVendedores");
  var vendedores = [
    { nombre: "Vendedor 1", correo: "vendedor1@example.com" },
    { nombre: "Vendedor 2", correo: "vendedor2@example.com" },
    { nombre: "Vendedor 3", correo: "vendedor3@example.com" },
    { nombre: "Vendedor 4", correo: "vendedor4@example.com" },
    { nombre: "Vendedor 5", correo: "vendedor5@example.com" },
    { nombre: "Vendedor 1", correo: "vendedor1@example.com" },
    { nombre: "Vendedor 2", correo: "vendedor2@example.com" },
    { nombre: "Vendedor 3", correo: "vendedor3@example.com" },
    { nombre: "Vendedor 4", correo: "vendedor4@example.com" }
  ];

  for (var i = 0; i < vendedores.length; i++) {
    var vendedorDiv = document.createElement("div");
    vendedorDiv.className = "vendedor";
    vendedorDiv.id = "vendedor" + i;

    var icono = document.createElement("img");
    icono.src = "icon/usuarioEjemplo.svg";
    icono.alt = "salir";
    icono.className = "icono";

    var lista = document.createElement("ul");
    lista.className = "listaVendedor";

    var nombreLi = document.createElement("li");
    nombreLi.className = "nombre";
    nombreLi.textContent = vendedores[i].nombre;

    var correoLi = document.createElement("li");
    correoLi.className = "correo";
    correoLi.textContent = vendedores[i].correo;

    lista.appendChild(nombreLi);
    lista.appendChild(correoLi);

    vendedorDiv.appendChild(icono);
    vendedorDiv.appendChild(lista);

  
    var modificarDiv = document.createElement("div");
    modificarDiv.className = "modificarDiv";

    var modificar = document.createElement("img");
    modificar.src = "../static/IMAGE.SVG/eliminarIcon.svg";
    modificar.alt = "eliminar";
    modificar.className = "modificar";

    modificarDiv.appendChild(modificar);
    modificar.addEventListener("click", function() {
    eliminarVendedor(this.parentNode.parentNode.id);
    });

    vendedorDiv.appendChild(modificarDiv);
    

    contenedor.appendChild(vendedorDiv);
  }
}

function eliminarVendedor(vendedorId) {
  var vendedor = document.getElementById(vendedorId);
  vendedor.remove();
}

function buscarVendedor(event) {
  event.preventDefault();

  var nombreBuscado = document.querySelector("input[type='text']").value;

  var vendedores = document.getElementsByClassName("vendedor");
  var encontrado = false;

  for (var i = 0; i < vendedores.length; i++) {
    var nombreVendedor = vendedores[i].querySelector(".nombre").textContent;

    if (nombreVendedor === nombreBuscado) {
      encontrado = true;
      var vendedorId = vendedores[i].id;
      var vendedor = document.getElementById(vendedorId);
      vendedor.scrollIntoView({ behavior: "smooth" });
      break;
    }
  }

  if (!encontrado) {
    alert("Vendedor no encontrado");
  }
}

var formulario = document.querySelector("form");
formulario.addEventListener("submit", buscarVendedor);

tipodeRol();
generarVendedores();

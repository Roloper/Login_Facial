// Obtener elementos del DOM
const combo = document.getElementById('combo');
const cantidadInput = document.getElementById('cantidad');
const precioInput = document.getElementById('precio');
const stockInput = document.getElementById('stock');
const añadirBtn = document.querySelector('.Añadir button');
const tabla = document.querySelector('.Tabla4 table');
const totalSpan = document.getElementById('total-span');

// Datos de productos (puedes reemplazar esto con tus propios datos)
const productos = [
  { opcion: 'opcion1', precio: 10.00, stock: 5 },
  { opcion: 'opcion2', precio: 15.00, stock: 8 },
  { opcion: 'opcion3', precio: 20.00, stock: 3 }
];

// Actualizar el stock y el precio al seleccionar una opción
combo.addEventListener('change', () => {
  const opcionSeleccionada = combo.value;
  const producto = productos.find(p => p.opcion === opcionSeleccionada);

  if (producto) {
    precioInput.value = producto.precio.toFixed(2);
    stockInput.value = producto.stock.toFixed(2);
  }
});

// Manejar el evento de clic en el botón "Añadir Producto"
añadirBtn.addEventListener('click', () => {
  const opcionSeleccionada = combo.value;
  const producto = productos.find(p => p.opcion === opcionSeleccionada);
  const cantidad = parseFloat(cantidadInput.value);

  if (producto && cantidad && cantidad > 0 && producto.stock >= cantidad) {
    const filas = tabla.querySelectorAll('tr');
    let filaExistente = null;

    // Buscar una fila existente con celdas vacías
    for (let i = 1; i < filas.length; i++) {
      const fila = filas[i];
      const descripcionTd = fila.querySelector('td:nth-child(1)');
      const cantidadTd = fila.querySelector('td:nth-child(2)');
      const precioTd = fila.querySelector('td:nth-child(3)');
      const importeTd = fila.querySelector('td:nth-child(4)');

      if (
        descripcionTd.textContent.trim() === '' &&
        cantidadTd.textContent.trim() === '' &&
        precioTd.textContent.trim() === '' &&
        importeTd.textContent.trim() === ''
      ) {
        filaExistente = fila;
        break;
      }
    }

    if (filaExistente) {
      // Rellenar los datos en la fila existente
      const descripcionTd = filaExistente.querySelector('td:nth-child(1)');
      const cantidadTd = filaExistente.querySelector('td:nth-child(2)');
      const precioTd = filaExistente.querySelector('td:nth-child(3)');
      const importeTd = filaExistente.querySelector('td:nth-child(4)');
      const eliminarTd = filaExistente.querySelector('td:nth-child(5)');

      descripcionTd.textContent = opcionSeleccionada;
      cantidadTd.textContent = cantidad;
      precioTd.textContent = producto.precio.toFixed(2);
      importeTd.textContent = calcularImporte(cantidad, producto.precio).toFixed(2);

      eliminarTd.innerHTML = '<img src="icon/eliminaricon.svg" alt="Eliminar" class="imagen-pequena">';
      eliminarTd.addEventListener('click', eliminarCompra.bind(null, filaExistente));
    } else {
      // Crear una nueva fila en la tabla
      const fila = crearNuevaFila(opcionSeleccionada, cantidad, producto);
      tabla.appendChild(fila);
    }

    producto.stock -= cantidad;

    actualizarTotal();

    cantidadInput.value = '';
    stockInput.value = producto.stock.toFixed(2);
  }
});

function calcularImporte(cantidad, precio) {
  return cantidad * precio;
}

function actualizarTotal() {
  const filas = tabla.querySelectorAll('tr');
  let total = 0;

  for (let i = 1; i < filas.length; i++) {
    const fila = filas[i];
    const importeTd = fila.querySelector('td:nth-child(4)');
    const importe = parseFloat(importeTd.textContent);

    if (!isNaN(importe)) {
      total += importe;
    }
  }

  totalSpan.textContent = total.toFixed(2);
}

function eliminarCompra(fila) {
  const cantidadTd = fila.querySelector('td:nth-child(2)');
  const producto = productos.find(p => p.opcion === fila.querySelector('td:nth-child(1)').textContent);
  const cantidad = parseFloat(cantidadTd.textContent);

  fila.remove();

  producto.stock += cantidad;

  actualizarTotal();

  stockInput.value = producto.stock.toFixed(2);
}

function crearNuevaFila(opcion, cantidad, producto) {
  const fila = document.createElement('tr');

  const descripcionTd = document.createElement('td');
  descripcionTd.textContent = opcion;

  const cantidadTd = document.createElement('td');
  cantidadTd.textContent = cantidad;

  const precioTd = document.createElement('td');
  precioTd.textContent = producto.precio.toFixed(2);

  const importeTd = document.createElement('td');
  importeTd.textContent = calcularImporte(cantidad, producto.precio).toFixed(2);

  const eliminarTd = document.createElement('td');
  const eliminarImg = document.createElement('img');
  eliminarImg.src = 'icon/eliminaricon.svg';
  eliminarImg.alt = 'Eliminar';
  eliminarImg.classList.add('imagen-pequena');
  eliminarTd.appendChild(eliminarImg);

  eliminarTd.addEventListener('click', eliminarCompra.bind(null, fila));

  fila.appendChild(descripcionTd);
  fila.appendChild(cantidadTd);
  fila.appendChild(precioTd);
  fila.appendChild(importeTd);
  fila.appendChild(eliminarTd);

  return fila;
}


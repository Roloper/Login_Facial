document.getElementById("guardarButton").addEventListener("click", function(event) {
    event.preventDefault(); // Evita que se realice la acción por defecto del botón (enviar el formulario)
  
    // Obtener los valores de los campos de texto
    var nombre = document.getElementById("nombreInput").value;
    var email = document.getElementById("emailInput").value;
    var password = document.getElementById("passwordInput").value;
  
    // Validar los campos
    if (nombre.trim() === "" || email.trim() === "" || password.trim() === "") {
      alert("Por favor, complete todos los campos.");
      return;
    }
  
    // Validar el correo electrónico
    if (!email.includes("@")) {
      alert("El correo electrónico debe contener el símbolo '@'.");
      return;
    }
  
    // Mostrar el mensaje de éxito
    var mensajeExito = document.getElementById("mensajeExito");
    mensajeExito.textContent = "Se han guardado los datos satisfactoriamente.";
  });
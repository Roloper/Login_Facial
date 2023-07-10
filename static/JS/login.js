const emailInput = document.querySelector('.email-8vT');
const passwordInput = document.querySelector('.password-ygB');
const errorContainer = document.createElement('div');
const errorMessage = document.createElement('div');
let errorDisplayed = false;


const usuarioCorrecto = 'ejemplo@gmail.com';
const contrasenaCorrecta = 'root';


errorContainer.classList.add('error-message');


function iniciarSesion() {
  const email = emailInput.value;
  const password = passwordInput.value;


  if (email === usuarioCorrecto && password === contrasenaCorrecta) {
    window.location.href = 'index.html';
  } else {
    if (!errorDisplayed) {
      errorMessage.textContent = 'El correo electrónico o la contraseña que has introducido son incorrectas ¡VUELVE A INTERTARLO!';
      errorContainer.appendChild(errorMessage);
      document.querySelector('.login-HXD').appendChild(errorContainer);
      errorDisplayed = true;
    }

    emailInput.style.color = '#AA0000';
    passwordInput.style.color = '#AA0000';
  }
}


function limpiarCampos() {
    if (errorDisplayed) {
      emailInput.value = '';
      passwordInput.value = '';
      emailInput.style.color = '';
      passwordInput.style.color = '';
      errorContainer.removeChild(errorMessage);
      errorDisplayed = false;
    }
  }
  
  emailInput.addEventListener('click', limpiarCampos);
  passwordInput.addEventListener('click', limpiarCampos);
  document.querySelector('.iniciar-sesin-urf button').addEventListener('click', iniciarSesion);
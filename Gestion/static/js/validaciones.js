// Hay muchas formas de elegir un nodo DOM; aquí obtenemos el formulario y, a continuación, el campo de entrada
// del correo electrónico, así como el elemento span en el que colocaremos el mensaje de error.
const form  = document.getElementsByTagName('form')[0];

const nombretarjeta = document.getElementById('nombretar');
const nombreTarjetaError = document.querySelector('#nombretar + span.error');

nombretarjeta.addEventListener('input', function (event) {
  // Cada vez que el usuario escribe algo, verificamos si
  // los campos del formulario son válidos.

    if (nombretarjeta.validity.valid) {
    // En caso de que haya un mensaje de error visible, si el campo
    // es válido, eliminamos el mensaje de error.
        nombreTarjetaError.innerHTML = ''; // Restablece el contenido del mensaje
        nombreTarjetaError.className = 'error'; // Restablece el estado visual del mensaje
    } else {
    // Si todavía hay un error, muestra el error exacto
        showError();
  }
});

form.addEventListener('submit', function (event) {
  // si el campo de correo electrónico es válido, dejamos que el formulario se envíe

    if(!nombretarjeta.validity.valid) {
    // Si no es así, mostramos un mensaje de error apropiado
        showError();
    // Luego evitamos que se envíe el formulario cancelando el evento
        event.preventDefault();
  }
});

function showError() {
    if(nombretarjeta.validity.valueMissing) {
    // Si el campo está vacío
    // muestra el mensaje de error siguiente.
    nombreTarjetaError.textContent = 'Debe introducir el nombre que aparece en la tarjeta';
    } else if(nombretarjeta.validity.typeMismatch) {
    // Si el campo no contiene una dirección de correo electrónico
    // muestra el mensaje de error siguiente.
    nombreTarjetaError.textContent = 'El valor introducido debe ser una dirección de correo electrónico.';
    } else if(nombretarjeta.validity.tooShort) {
    // Si los datos son demasiado cortos
    // muestra el mensaje de error siguiente.
    nombreTarjetaError.textContent = 'El correo electrónico debe tener al menos ${ nombretar.minLength } caracteres; ha introducido ${ nombretar.value.length }.';
    }

  // Establece el estilo apropiado
    nombreTarjetaError.className = 'error activo';
}
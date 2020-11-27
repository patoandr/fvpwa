// Nos permite solo ingresar letras que no permitan numeros.
function soloLetras(e) {
    var key = e.keyCode || e.which,
      tecla = String.fromCharCode(key).toLowerCase(),
      letras = " áéíóúabcdefghijklmnñopqrstuvwxyz",
      especiales = [8, 37, 39, 46],
      tecla_especial = false;

    for (var i in especiales) {
      if (key == especiales[i]) {
        tecla_especial = true;
        break;
      }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
      return false;
    }
  }

  function validarContraseña(e) {
    a= document.getElementById("id_password1").value ;
    b = document.getElementById("id_password2").value;
    if(a === b ){

    }else{
      alert("Las constraseñas no coinciden");
      document.getElementById("id_password1").focus();
      document.getElementById("id_password1").value = "";
      document.getElementById("id_password2").value = "";
      e.preventDefault();
      someBug();
      return false;
    }
}


      
  
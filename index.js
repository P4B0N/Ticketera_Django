//VALIDACION DE LOS CAMPOS DEL FORMULARIO

function validar() {
  
  var nombre = document.getElementById("nombre").value;
  var telefono = document.getElementById("telefono").value;
  var email = document.getElementById("email").value;
  var edad = document.getElementById("edad").value;
  var mensaje = document.getElementById("mensaje");
  var expresionR = /\w+@\w+\.+[a-z]/;//EXPRESION REGULAR = LETRAS Y NUMEROS, "@", LETRAS Y NUMEROS, "." Y LETRAS.

  if (nombre === "" || telefono === "" || email === "" || edad === "" || mensaje === "") {
    alert("Todos los campos son necesarios.");
    return false;//SI TODOS CAMPOS LLENOS
  }
  else if (nombre.length > 30) {
    alert("Nombre es demasido largo.");
    e.preventDefault(); 
    return false;//HASTA 30 CARACTERES
  }
  else if (telefono.length > 15) {
    alert("Telefono es demasido largo.");
    e.preventDefault(); 
    return false;//HASTA 15 CARACTERES
  }
  else if (isNaN(telefono)) {
    alert("Telefono debe ser un número.");
    e.preventDefault(); 
    return false;//SI ES NUMERO
  }
  else if (email.length > 100) {
    alert("Email es demasido largo.");
    e.preventDefault();
    return false;//HASTA 100 CARACTERES
  }
  else if (!expresionR.test(email)) {
    alert("Email no es valido.");
    document.formulario.email.focus();
    e.preventDefault(); 
    return false;//EXPRESION REGULAR 
  }
  else if (edad.length > 3) {
    alert("Edad es demasido largo.");
    e.preventDefault(); 
    return false;//HASTA 3 CARACTERES
  }
  else if (isNaN(edad)) {
    alert("Edad debe ser un número.");
    e.preventDefault(); 
    return false;//SI ES NUMERO
  }
  else if (edad<17) {
    alert("Debe ser mayor de edad.");
    e.preventDefault(); 
    return false;//SI ES MAYOR DE EDAD
  }
  else if (mensaje.lenngth > 250) {
    alert("Mensaje es demasido largo.");
    e.preventDefault(); 
    return false;//HASTA 250 CARACTERES
  }
}

//MENU AMBURGUESA
const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-menu");

navToggle.addEventListener("click", () => {
  navMenu.classList.toggle("nav-menu_visible");

//SE LE AGREGA UN ATRIBUTO PARA SER LEIDO POR LA TECLA ALT EN MODO ACCESIBLE
  if (navMenu.classList.contains("nav-menu_visible")) {
    navToggle.setAttribute("aria-label", "Cerrar menú");
  } else {
    navToggle.setAttribute("aria-label", "Abrir menú");
  }
});
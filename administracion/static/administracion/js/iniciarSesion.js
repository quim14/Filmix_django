document.addEventListener("DOMContentLoaded", function(){
    document.querySelector('#form-iniciar').addEventListener('submit',validarInicio);
});

function validarInicio(evento) {
    evento.preventDefault();
    var email = document.querySelector('#iniciar-email');
    if (email.value.length == 0 ){
        alert('El campo e-mail está vacio');
        return;
    }
    var pass = document.querySelector('#iniciar-pass');
    if (pass.value.length == 0 ){
        alert('El campo contraseña está vacio');
        return;
    }
    this.submit();
}
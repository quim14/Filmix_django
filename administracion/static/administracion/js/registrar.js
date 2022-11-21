document.addEventListener("DOMContentLoaded", function(){
    document.querySelector('#form-registrar').addEventListener('submit',validarRegistro);
});

function validarRegistro(evento) {
    evento.preventDefault();
    var nombre = document.querySelector('#reg-nombre');
    if (nombre.value.length == 0 ){
        alert('Por favor, ingrese su nombre');
        return;
    }
    else if (nombre.value.length > 20){
        alert('Solo puede ingresar 20 caracteres como máximo en nombre');
        return;
    }
    var apellido = document.querySelector('#reg-apellido');
    if (apellido.value.length == 0 ){
        alert('Por favor, ingrese su apellido');
        return;
    }
    else if (apellido.value.length > 20){
        alert('Solo puede ingresar 20 caracteres como máximo en apellido');
        return;
    }
    var email = document.querySelector('#reg-email');
    if (email.value.length == 0 ){
        alert('Por favor, ingrese un e-mail');
        return;
    }
    var pass = document.querySelector('#reg-pass');
    if (pass.value.length == 0 ){
        alert('Por favor, ingrese una contraseña');
        return;
    }
    else if (pass.value.length < 6){
        alert('La contraseña debe tener como mínimo 6 caracteres');
        return;
    }
    else if (pass.value.includes(' ')){
        alert('La contraseña no debe tener espacios');
        return;
    }
    var conf = document.querySelector('#conf-pass');
    if (conf.value.length == 0 ){
        alert('Por favor, confirme la contraseña');
        return;
    }
    else if (conf.value != pass.value){
        alert('La contraseña no coincide con la confirmación');
        return;
    }
    this.submit();
}
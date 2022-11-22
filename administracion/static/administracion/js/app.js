addEventListener('DOMContentLoaded', ()=>{
    const btn_menu = document.querySelector('.btn-menu');
    if(btn_menu){
        btn_menu.addEventListener('click',()=>{
            const opciones = document.querySelector('.nav-links');
            opciones.classList.toggle('show');
        })
    }
})
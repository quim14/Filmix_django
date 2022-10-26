// Se cargan los datos de las peliculas
var pelicula_0 = {
    id: 1,
    nombre: "Granizo",
    imagen: "./img/Peliculas/Granizo.jpg",
    fecha_ini: "01/03/2022",
    fecha_fin: "31/12/2022",
    horarios: ["20:00","22:00"],
    descripcion: "Un famoso meteorólogo de la televisión se convierte en el enemigo público número uno cuando no logra evitar una terrible tormenta de granizo.",
    trailer: "https://www.youtube.com/embed/-F2watcvQQs",
}
var pelicula_1 = {
    id: 2,
    nombre: "Doctor Strange en el mutiverso de la locura",
    imagen: "./img/Peliculas/Doctor_Strange2.jpg",
    fecha_ini: "01/05/2022",
    fecha_fin: "31/12/2022",
    horarios: ["16:00","19:00","21:00"],
    descripcion: "El Dr. Stephen Strange abre un portal al multiverso al utilizar un hechizo prohibido. Ahora su equipo debe enfrentarse a una amenaza enorme.",
    trailer: "https://www.youtube.com/embed/aWzlQ2N6qqg",
}
var pelicula_2 = {
    id: 3,
    nombre: "Animales Fantásticos: Los secretos de Dumbledore",
    imagen: "./img/Peliculas/Animales_Fantasticos3.jpg",
    fecha_ini: "01/03/2022",
    fecha_fin: "01/06/2022",
    horarios: ["17:00","20:00"],
    descripcion: "Ante una severa amenaza, el magizoólogo Newt Scamander lidera a un valiente grupo de magos y brujas que busca detener al malvado Gellert Grindelwald.",
    trailer: "https://www.youtube.com/embed/QfYgcLuxS5Y",
}
var pelicula_3 = {
    id: 4,
    nombre: "El peso del talento",
    imagen: "./img/Peliculas/El-peso-del-talento.jpg",
    fecha_ini: "01/05/2022",
    fecha_fin: "01/01/2023",
    horarios: ["15:30","21:30"],
    descripcion: 'Un famoso meteorólogo de la televisión se convierte en el enemigo público número uno cuando no logra evitar una terrible tormenta de granizo.',
    trailer: "https://www.youtube.com/embed/x2YHPZMj8r4",
}
var pelicula_4 = {
    id: 5,
    nombre: "Lightyear",
    imagen: "./img/Peliculas/Lightyear.jpg",
    fecha_ini: "10/06/2022",
    fecha_fin: "01/02/2023",
    horarios: ["15:00","17:00","21:00"],
    descripcion: 'La historia del origen de Buzz Lightyear y sus aventuras hasta el infinito y más allá.',
    trailer: "https://www.youtube.com/embed/tjcrjrX9Nfo",
}
var pelicula_5 = {
    id: 6,
    nombre: "Sonic 2, la película",
    imagen: "./img/Peliculas/Sonic2.jpg",
    fecha_ini: "01/04/2022",
    fecha_fin: "31/12/2022",
    horarios: ["20:30","16:30"],
    descripcion: 'Después de establecerse en Green Hills, Sonic quiere demostrar que tiene madera de héroe. La prueba de fuego llega con el retorno del malvado Robotnik, y su nuevo compinche, Knuckles, en busca de una esmeralda que destruye civilizaciones.',
    trailer: "https://www.youtube.com/embed/hB6krsAiyFo",
}
var pelicula_6 = {
    id: 7,
    nombre: "La médium",
    imagen: "./img/Peliculas/The_Medium.jpg",
    fecha_ini: "01/04/2022",
    fecha_fin: "09/06/2022",
    horarios: ["21:30","23:00"],
    descripcion: 'En Tailandia, un grupo de documentalistas registra la vida cotidiana de una médium, Nim Tonvali, quien relata estar poseída por el espíritu de la diosa Bayan. Durante el velatorio de su cuñado, Nim observa un comportamiento extraño en su sobrina.',
    trailer: "https://www.youtube.com/embed/XStLMJu0fI4",
}
var pelicula_7 = {
    id: 8,
    nombre: "Top Gun: Maverick",
    imagen: "./img/Peliculas/Top_Gun_Maverick.jpg",
    fecha_ini: "01/05/2022",
    fecha_fin: "31/12/2022",
    horarios: ["18:00","20:00","22:00"],
    descripcion: 'Tras más de 30 años de servicio como uno de los mejores aviadores de la Armada, Pete "Maverick" Mitchel se encuentra dónde siempre quiso estar, empujando los límites como un valiente piloto de prueba.',
    trailer: "https://www.youtube.com/embed/zzBIzYmxatU",
}
// ----------VARIABLES----------------
const peliculas = [];
peliculas.push(pelicula_0, pelicula_1, pelicula_2, pelicula_3, pelicula_4, pelicula_5, pelicula_6, pelicula_7);
var cartelera = document.querySelector(".peliculas");
var detallePelicula = document.querySelector('#detalle-peliculas');


//-------------FUNCIONES----------------
var mostrarCartelera = () =>
{
    cartelera.innerHTML='';
    let pelic;
    for (let pelicula in peliculas){
        cartelera.innerHTML = cartelera.innerHTML + `
        <div class="pelicula-item" id=${peliculas[pelicula].id}>
            <a href="./detalle-pelicula.html" class="">
                <img src=${peliculas[pelicula].imagen} alt="">
                <div class="detalle-pelicula">
                    <p class="pelicula-titulo">${peliculas[pelicula].nombre}</p>
                </div>
            </a>    
        </div>
        `;
    }
    var items = document.querySelectorAll(".pelicula-item");
    for (let item in items){
        if (items[item].id){
            items[item].addEventListener('click', function(){
                sessionStorage.setItem("detalle", JSON.stringify(peliculas[item]));
            });
        }
    }
}
mostrarCartelera();





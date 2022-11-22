var detalle =  JSON.parse(sessionStorage.getItem("detalle"));
console.log(detalle);
var pelicula = document.querySelector(".detalle-grid");
var horarios ='';
for (let i in detalle.horarios){
    horarios = horarios + `<label class="hora" for="">${detalle.horarios[i]}</label>`;
}

pelicula.innerHTML = `
    <div class="g-img">
        <img src=${detalle.imagen} alt="">
    </div>
    <div class="g-det">
        <h2>${detalle.nombre}</h2>
    </div>
    <div class="g-det">
        <label for="">${detalle.descripcion}</label>
    </div>
    <div class="g-det">
        ${horarios}
    </div>
    <div class="g-frame">
        <iframe 
            src=${detalle.trailer} 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>
    </div>
`;

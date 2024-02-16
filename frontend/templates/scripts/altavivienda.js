function guardarTipoVivienda(li){
    let secTipoVivienda = document.getElementById('secTipoVivienda');
    let secVenderAlquilar = document.getElementById('secVenderAlquilar');
    let tipoVivienda = li.dataset.value;
    let input = document.getElementById('tipoVivienda');
    input.value = tipoVivienda;
    secTipoVivienda.setAttribute('style', 'display:none');
    secVenderAlquilar.removeAttribute('style');
}

function guardarVenderAlquilar(li){
    let secDireccion = document.getElementById('secDireccion');
    let secVenderAlquilar = document.getElementById('secVenderAlquilar');
    let tipoVivienda = li.dataset.value;
    let input = document.getElementById('venderAlquilar');
    input.value = tipoVivienda;
    secVenderAlquilar.setAttribute('style', 'display:none');
    secDireccion.removeAttribute('style');
}


 function continuarDireccion(){
    let secDireccion = document.getElementById('secDireccion');
    let secCaracteristicas = document.getElementById('secCaracteristicas');
    secDireccion.setAttribute('style', 'display:none');
    secCaracteristicas.removeAttribute('style');

}


function continuarCaracteristicas(){
    let secNombre = document.getElementById('secNombre'); 
    let secCaracteristicas = document.getElementById('secCaracteristicas');
    secCaracteristicas.setAttribute('style', 'display:none');
    secNombre.removeAttribute('style');    
    
}

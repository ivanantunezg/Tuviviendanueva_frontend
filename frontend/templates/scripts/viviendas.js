document.addEventListener('DOMContentLoaded', function() {
    const labelAnio = document.querySelectorAll('.lblAnio');

    labelAnio.forEach(label => {
        label.addEventListener('click', event => {
            let id = event.currentTarget.getAttribute('data-name');
            let chk = document.getElementById(id);
            toggleCheckbox(chk);
        });
    });

    const lblTipoCasa = document.querySelectorAll('.lblTipoCasa');

    lblTipoCasa.forEach(label => {
        label.addEventListener('click', event => {
            let id = event.currentTarget.getAttribute('data-name');
            let chk = document.getElementById(id);
            toggleCheckbox(chk);
        });
    });

});

function toggleCheckbox(chk){
    if (!chk.checked)
        chk.setAttribute("checked","checked")
    else
        chk.removeAttribute("checked")
}


document.addEventListener("DOMContentLoaded", function() {
    cargarFiltros();
});

function cargarFiltros(){
    var inputs = document.querySelectorAll('input');
    const url = new URL(window.location.href);
    inputs.forEach(function(input) {
        if(url.searchParams.get(input.name)){
            input.value = url.searchParams.get(input.name);
        }
    });
}
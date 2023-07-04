const div = document.querySelector('.div-img-principal');
const imgSrc = div.getAttribute('data-imgSrc');
div.style.setProperty('--imgSrc', `url(${imgSrc})`);

const divSec = document.querySelector('.div-img-secundarias');
const imgSrcSecundaria = divSec.getAttribute('data-imgSrcSecundaria');
divSec.style.setProperty('--imgSrcSecundaria', `url(${imgSrcSecundaria})`);
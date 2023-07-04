const div = document.querySelector('.img-vivienda');
const imgSrc = div.getAttribute('data-imgSrc');
div.style.setProperty('--imgSrc', `url(${imgSrc})`);


window.addEventListener('DOMContentLoaded', function() {
    var container = document.querySelector('body');
    var footer = document.querySelector('footer');
  
    function adjustFooterPosition() {
      var containerHeight = container.clientHeight;
      var windowHeight = window.innerHeight;
  
      if (containerHeight > windowHeight) {
        footer.style.position = 'relative';
      } else {
        footer.style.position = 'absolute';
      }
    }
  
    adjustFooterPosition(); // Llamamos a la función al cargar la página
  
    // Llamamos a la función cada vez que se redimensiona la ventana
    window.addEventListener('resize', adjustFooterPosition);
  });
// reference to codepen

$(document).ready(function() {
    var header = $('.header'),
                prevScrollTop = $(window).scrollTop(),
        tallHeight = 300,
        shortHeight = 100,
        diff = tallHeight - shortHeight,
        delay = 2;
        
    
      $(window).scroll(function(event) {
         var currScrollTop = $(this).scrollTop(),
          increment = currScrollTop / delay;
      header.css({ 'background-color' : 'rgba(238,238,239,' + (increment/diff) + ')',
                   'box-shadow'       : '0 0 3px rgba(165, 165, 165,' + (increment/diff) + ')',
                    'border-bottom'   : 'solid 5px rgba(151, 242, 243,' + (increment/diff) + ')',});
      header.height(tallHeight - increment);
      });
  });
// Initialize WOW js
wow = new WOW(
  {
  boxClass:     'wow',      
  animateClass: 'animated', 
  offset:       0,          
  mobile:       true,       
  live:         true      
    }
)
wow.init();

$.extend($.expr[':'], {
  startsWith: function(elem,match) {  
      return (elem.textContent || elem.innerText || "").indexOf(match[3]) == 0;
  }  
});

// Change post-tag color depending on Category
$('.post-tag span:contains("Restaurants")').css("background","var(--restaurants)");
$('.post-tag span:contains("Terraces")').css("background","var(--terraces)");
$('.post-tag span:contains("Nightlife")').css("background","var(--nightlife)");
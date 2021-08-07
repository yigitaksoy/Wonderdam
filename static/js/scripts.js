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

// Password match input validation for registration form
$('#password, #confirm_password').on('keyup', function () {
  if ($('#password').val() == $('#confirm_password').val()) {
    $('#confirm-input').html('Passwords Match!').css('color', 'green');
  } else 
    $('#confirm-input').html('Password Dont Match!').css('color', 'var(--error)');
});

// Word counter for blog post textarea
function countChars(obj){
  var maxLength = 1500;
  var strLength = obj.value.length;
  
  document.getElementById("counter").innerHTML = strLength+' out of '+maxLength+' characters';
  }

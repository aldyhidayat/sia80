const menuToggle = document.querySelector('.menu-toggle');
const ulMenu = document.getElementById('ulmenu');
const container = document.querySelector('.container')
menuToggle.addEventListener('click', function(){
    ulMenu.classList.toggle('slide');
    container.classList.toggle('slide');
});

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }
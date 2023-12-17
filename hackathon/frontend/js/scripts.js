// index js
// carousel    
$(document).ready(function() {
    // enabling the carousel
    $('#myCarousel').carousel();

    // interval for automatic sliding (milliseconds)
    setInterval(function() {
        $('#myCarousel').carousel('next');
    }, 5000);

// dropdown menu
    // Add an event listener to the navbar-toggler button
    document.querySelector('.navbar-toggler').addEventListener('click', function() {
        // Toggle the 'toggled' class on the navbar-collapse element
        document.querySelector('.navbar-collapse').classList.toggle('toggled');
    });
        });


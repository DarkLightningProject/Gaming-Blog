document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners for all like buttons
    document.querySelectorAll('.like-btn').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior
            button.classList.add('clicked');
            setTimeout(function() {
                button.classList.remove('clicked');
                window.location.href = button.href; // Follow the link after animation
            }, 200); // Match this duration with the CSS transition time
        });
    });

    // Add event listeners for all dislike buttons
    document.querySelectorAll('.dislike-btn').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior
            button.classList.add('clicked');
            setTimeout(function() {
                button.classList.remove('clicked');
                window.location.href = button.href; // Follow the link after animation
            }, 200); // Match this duration with the CSS transition time
        });
    });
});

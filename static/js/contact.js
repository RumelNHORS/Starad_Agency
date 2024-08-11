
$(document).ready(function() {
    $('#contact-form').on('submit', function(e) {
        e.preventDefault(); // Prevent default form submission

        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                // Show the success modal
                $('#successModal').modal('show');

                // Optionally, reset the form fields
                $('#contact-form')[0].reset();
            },
            error: function(xhr, status, error) {
                // Show an error modal or handle the error accordingly
                alert('An error occurred: ' + error);
            }
        });
    });
});


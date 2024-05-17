document.getElementById('kycForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Form fields
    const fields = [
        'firstName', 'lastName', 'dob', 'gender',
        'country', 'town', 'state', 'zip',
        'phone1', 'email'
    ];

    let isValid = true;

    // Validate fields
    fields.forEach(function(fieldId) {
        const field = document.getElementById(fieldId);
        if (field.value.trim() === '' || (field.tagName === 'SELECT' && field.value === '')) {
            field.classList.remove('is-valid');
            field.classList.add('is-invalid');
            isValid = false;
        } else {
            field.classList.remove('is-invalid');
            field.classList.add('is-valid');
        }
    });

    // Display alert based on validation
    const alertPlaceholder = document.getElementById('alertPlaceholder');
    if (isValid) {
        alertPlaceholder.innerHTML = `
            <div class="alert alert-success alert-dismissible fade show" role="alert">
                <strong>Success!</strong> Your data has been submitted.
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;
        // Optionally, you can clear the form here if needed
        // document.getElementById('kycForm').reset();
        // Remove valid class after form reset
        fields.forEach(function(fieldId) {
            document.getElementById(fieldId).classList.remove('is-valid');
        });
    } else {
        alertPlaceholder.innerHTML = `
            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                <strong>Error!</strong> Please fill out all required fields.
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;
    }
});
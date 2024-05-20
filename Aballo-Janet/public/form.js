const form = document.getElementById('kycForm');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    if (validateForm()) {
        form.submit();
    } else {
        highlightInvalidFields();
    }
});

function validateForm() {
    const fullName = form.fullName.value.trim();
    const email = form.email.value.trim();
    const phone = form.phone.value.trim();
    const address = form.address.value.trim();
    const dob = form.dob.value.trim();
    const nationality = form.nationality.value.trim();

    if (fullName === '' || email === '' || phone === '' || address === '' || dob === '' || nationality === '') {
        return false; 
    }

    return true; 
}

function highlightInvalidFields() {
    const formGroups = document.querySelectorAll('.form-group');

    formGroups.forEach(function(formGroup) {
        const input = formGroup.querySelector('input, select');
        const isValid = input.value.trim() !== ''; 

        if (!isValid) {
            formGroup.classList.add('invalid');
        } else {
            formGroup.classList.remove('invalid');
        }
    });
}

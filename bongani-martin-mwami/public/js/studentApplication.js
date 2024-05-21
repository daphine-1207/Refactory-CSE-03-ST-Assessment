function validateForm() {
    const form = document.getElementById('students');
    const inputs = form.querySelectorAll('input, autoSizingselect');
    let isValid = true;

    inputs.forEach(input => {
        if (input.value.trim() === '') {
            isValid = false;
            input.style.border = '1px solid red';
        } else {
            input.style.border = '1px solid #ccc';
        }
    });

    if (!isValid) {
        return false;
    }
}

   

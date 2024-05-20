const validation = (event) => {
    let error = 0;
  
    // First Name validation
    const firstName = document.getElementById('firstName');
    const firstNameError = document.getElementById('firstNameError');
    if (firstName.value.trim() === '') {
        firstName.style.border = '1px solid red';
        firstNameError.textContent = 'Invalid field!';
        firstNameError.style.color = 'red';
        error++;
    } else {
        firstName.style.border = '1px solid green';
        firstNameError.textContent = '';
    }

    //Last Name validation
    const lastName = document.getElementById('lastName');
    const lastNameError = document.getElementById('lastNameError');
    if (lastName.value.trim() === '') {
        lastName.style.border = '1px solid red';
        lastNameError.textContent = 'Invalid field!';
        lastNameError.style.color = 'red';
        error++;
    } else {
        lastName.style.border = '1px solid green';
        lastNameError.textContent = '';
    }

        //Residence validation
        const residence = document.getElementById('residence');
        const residenceError = document.getElementById('residenceError');
        if (residence.value.trim() === '') {
            residence.style.border = '1px solid red';
            residenceError.textContent = 'Invalid field!';
            residenceError.style.color = 'red';
            error++;
        } else {
            residence.style.border = '1px solid green';
            residenceError.textContent = '';
        }

        //Date of Birth validation
        const dob = document.getElementById('dob');
        const dobError = document.getElementById('dobError');
        if (dob.value.trim() === '') {
            dob.style.border = '1px solid red';
            dobError.textContent = 'Invalid field!';
            dobError.style.color = 'red';
            error++;
        } else {
            dob.style.border = '1px solid green';
            dobError.textContent = '';
        }

    if (error > 0) {
        event.preventDefault();
    }
  };
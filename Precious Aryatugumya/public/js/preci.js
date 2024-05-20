
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            let valid = true;

            // Validate first name
            const firstName = document.getElementById('firstName').value;
            if (!firstName) {
                document.getElementById('firstNameError').style.display = 'inline';
                valid = false;
            } else {
                document.getElementById('firstNameError').style.display = 'none';
            }

            // Validate last name
            const lastName = document.getElementById('lastName').value;
            if (!lastName) {
                document.getElementById('lastNameError').style.display = 'inline';
                valid = false;
            } else {
                document.getElementById('lastNameError').style.display = 'none';
            }

            // Validate course
            const course = document.getElementById('course').value;
            if (!course) {
                document.getElementById('courseError').style.display = 'inline';
                valid = false;
            } else {
                document.getElementById('courseError').style.display = 'none';
            }

            // Validate entry scheme
            const entryScheme = document.getElementById('entryScheme').value;
            if (!entryScheme) {
                document.getElementById('entrySchemeError').style.display = 'inline';
                valid = false;
            } else {
                document.getElementById('entrySchemeError').style.display = 'none';
            }

            // Validate intake
            const intake = document.getElementById('intake').value;
            if (!intake) {
                document.getElementById('intakeError').style.display = 'inline';
                valid = false;
            } else {
                document.getElementById('intakeError').style.display = 'none';
            }

            // Validate sponsorship
            const sponsorship = document.getElementById('sponsorship').value;
            if (!sponsorship) {
                document.getElementById('sponsorshipError').style.display = 'inline';
                valid = false;
            } else {
                document.getElementById('sponsorshipError').style.display = 'none';
            }

            // Validate gender
            const gender = document.getElementById('gender').value;
            if (!gender) {
                document.getElementById('genderError').style.display = 'inline';
                valid = false;
            } else {
                document.getElementById('genderError').style.display = 'none';
            }

            // Validate date of birth
            const dob = document.getElementById('dob').value;
            if (!dob) {
                document.getElementById('dobError').style.display = 'inline';
                valid = false;
            } else {
                document.getElementById('dobError').style.display = 'none';
            }

            // Validate residence (assuming zip code)
            const residence = document.getElementById('residence').value;
            const zipCodePattern = /^\d{5}(-\d{4})?$/; // US ZIP code pattern
            if (!zipCodePattern.test(residence)) {
                document.getElementById('residenceError').style.display = 'inline';
                valid = false;
            } else {
                    document.getElementById('residenceError').style.display = 'none';
                }
    
                // Validate terms and conditions agreement
                const agreeTerms = document.getElementById('agreeTerms').checked;
                if (!agreeTerms) {
                    document.getElementById('agreeTermsError').style.display = 'inline';
                    valid = false;
                } else {
                    document.getElementById('agreeTermsError').style.display = 'none';
                }
    
                if (!valid) {
                    event.preventDefault();
                }
            });
       

        document.addEventListener('DOMContentLoaded', function () {
            const form = document.getElementById('registrationForm');
            const nameInput = document.getElementById('name');
            const emailInput = document.getElementById('email');
            const passwordInput = document.getElementById('password');

            const nameError = document.getElementById('nameError');
            const emailError = document.getElementById('emailError');
            const passwordError = document.getElementById('passwordError');
            const successMessage = document.getElementById('successMessage');

            form.addEventListener('submit', function (event) {
                event.preventDefault();
                let isValid = true;

                // Clear previous error messages
                nameError.textContent = '';
                emailError.textContent = '';
                passwordError.textContent = '';
                successMessage.textContent = '';

                // Validate name
                if (nameInput.value.trim() === '') {
                    nameError.textContent = 'Name is required.';
                    isValid = false;
                }

                // Validate email
                if (emailInput.value.trim() === '') {
                    emailError.textContent = 'Email is required.';
                    isValid = false;
                } else if (!validateEmail(emailInput.value)) {
                    emailError.textContent = 'Please enter a valid email address.';
                    isValid = false;
                }

                // Validate password
                if (passwordInput.value.trim() === '') {
                    passwordError.textContent = 'Password is required.';
                    isValid = false;
                } else if (passwordInput.value.length < 6) {
                    passwordError.textContent = 'Password must be at least 6 characters long.';
                    isValid = false;
                }

                if (isValid) {
                    successMessage.textContent = 'Form submitted successfully!';
                    form.reset();
                }
            });

            function validateEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            }
        });

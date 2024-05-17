function validation(event) {
    event.preventDefault();
    let isValid = true;
  
    // Get form elements
    const form = document.forms['validationForm'];
    const elements = form.elements;
  
    // Check all inputs
    for (let element of elements) {
      if (element.type !== 'submit' && !element.value) {
        isValid = false;
        element.classList.add('is-invalid');
        element.classList.remove('is-valid');
      } else if (element.type !== 'submit') {
        element.classList.add('is-valid');
        element.classList.remove('is-invalid');
      }
    }
  
    const alertPlaceholder = document.getElementById('alertPlaceholder');
  
    // Show alert based on validation result
    if (isValid) {
      showAlert('Data has been submitted successfully!', 'success');
    } else {
      showAlert('Please fill out all fields.', 'danger');
    }
  
    return isValid;
  }
  
  function showAlert(message, type) {
    const alertPlaceholder = document.getElementById('alertPlaceholder');
    alertPlaceholder.innerHTML = `<div class="alert alert-${type} alert-dismissible" role="alert">
                                    ${message}
                                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                  </div>`;
  }
  
  // CSS to apply red/green borders
  const style = document.createElement('style');
  style.innerHTML = `
    .is-invalid { border-color: red; }
    .is-valid { border-color: green; }
  `;
  document.head.appendChild(style);
  
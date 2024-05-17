const fields = form.querySelectorAll('.form-control');

fields.forEach((field) => {
  field.addEventListener('blur', (e) => {
    console.log(field);
    if (!field.value) {
      field.setAttribute('class' ,'is-invalid form-control');
      field.parentNode.lastChild.innerHTML = 'This field is required';
    } else {
      field.setAttribute('class' ,'is-valid form-control');
      field.parentNode.lastChild.innerHTML = '';
    }
  });
});
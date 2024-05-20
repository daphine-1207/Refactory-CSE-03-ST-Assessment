let fullName = document.getElementById("firstName");
let fullNameError = document.getElementById("fullnameError");

const validation = (event) => {
   
  let error = 0;
  if (fullName.value == "") {
    fullName.style.border = "1px solid red";
    fullNameError.textContent = "Please enter Fullname";
    fullNameError.style = "color:red";
    error++;
  } else {
    fullName.style.border = "1px solid green";
    fullNameError.style = "";
  }

  if (error > 0){
    event.preventDefault()
  }
};

let firstName = document.getElementById('firstName'); //for input tag id
let lastName = document.getElementById('lastName'); //for input tag id
let address = document.getElementById("address");
let gender = document.getElementsByName("gender");




let firstNameError = document.getElementById('firstNameError'); //for small tag id
let lastNameError = document.getElementById('lastNameError'); //for small tag id
let addressError = document.getElementById("addressError");
let genderError = document.getElementById("genderError");


const validation = (event) => {
  let error = 0;

   //first Name validation
  if (firstName.value == "") {
    firstName.style.border = "1px solid red";
    firstNameError.textContent = "Please enter first Name!";
    firstNameError.style = "color: red;";
    error++;
    // error = error +1;
  } else {
    firstName.style.border = "1px solid green";
    firstNameError.textContent = "";
  }


    //lastName validation
  if (lastName.value == "") {
    lastName.style.border = "1px solid red";
    lastNameError.textContent = "Please enter Last Name!";
    lastNameError.style = "color: red;";
    error++;
  } else {
    userName.style.border = "1px solid green";
    userName.textContent = " ";
  }


   //residence validation
   if (residence.value == "") {
    residence.style.border = "1px solid red";
    residenceError.textContent = "Please enter residence!";
    residenceError.style = "color: red;";
    error++;
  } else {
    residence.style.border = "1px solid green";
    residence.textContent = " ";
  }

  // Radio buttons validation
  if (!formValid) {
    genderError.textContent = "Please select gender";
    genderError.style =
      "color:red; font-size:12px; font-family:Arial, Helvetica, Sans-serif";
    // return false;
    error++;
  } else {
    genderError.textContent = "";
  }
  if (error > 0) {
    event.preventDefault();
  }
};
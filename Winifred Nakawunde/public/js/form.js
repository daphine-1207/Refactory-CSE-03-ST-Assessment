
console.log('JavaScript is connected');
document.getElementById("student-form").addEventListener("submit",function(event){
    event.preventDefault();
    // Fetch all input values
    const firstname = document.getElementById("firstname").value;
    const lastname = document.getElementById("lastname").value;
    const course = document.getElementById("course").value;
    const entryscheme = document.getElementById("entryscheme").value;
    const intake = document.getElementById("intake").value;
    const scholarship = document.getElementById("scholarship").value;
    const gender = document.getElementById("gender").value;
    const dateOfBirth = document.getElementById("dateOfBirth").value;
    const residence = document.getElementById("residence").value;

    // Validation
    if (firstname === "" ||lastname === "" || course === "" || entryscheme === "" || intake=== "" || scholarship === "" || gender === "" || dateOfBirth === "" || residence ==="" ) {
        alert("Please fill in all required fields.");
        return;
    }
      
  
      document.getElementByid("student-form").reset();
      
  
});


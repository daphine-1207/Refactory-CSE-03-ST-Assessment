const express = require("express");
const router = express.Router();

// Import model
const StudentRegister = require('../models/StudentRegister');

// Student routes
router.get("/registerStudent", (req, res) => {
  res.render("studentApplicationForm");
});

// Installing async function
router.post(
  "/registerStudent",
  async (req, res) => {
    try {
      const student = new StudentRegister(req.body); // Create a new student registration document from the req body
      console.log(student); 
      await student.save(); // Save student reg document in db
      res.redirect("/registerStudent"); // Redirect to registerStudent route upon successful save
    } catch (error) {
      res.status(400).send("Sorry, something went wrong"); // Send status code 400 error message if something goes wrong
      console.log("Error registering the student", error);
    }
  }
);

module.exports = router;


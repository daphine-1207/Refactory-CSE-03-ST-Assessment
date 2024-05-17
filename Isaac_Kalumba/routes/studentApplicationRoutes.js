const express = require("express");
const router = express.Router();


//import model
const StudentRegistration = require("../models/StudentRegistration");

// Student application routes
router.get("/registerStudent", (req, res) => {
    res.render("applicationForm");
  });

  router.post("/registerStudent", async (req, res) => {
    try {
      const student = new StudentRegistration(req.body);
      console.log(student);
      await student.save();
      res.redirect("/registerStudent");
    } catch (error) {
      res.status(400).redirect("/registerStudent");
      console.log("Error submitting appication", error);
    }
  });


module.exports = router;

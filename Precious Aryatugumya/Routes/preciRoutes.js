const express = require("express");
const router = express.Router();

//import model
const registration = require("../models/preci");

router.get("/registerstudent",  (req, res) => {
  res.render("preci");
});

router.post( "/registersudent", async (req, res) => {
    try {
      const student = new registration(req.body);
      await student.save();
      console.log(student);
      res.redirect("");
    } catch (error) {
      res.status(400).send("sorry something went wrong");
      console.log("error registering student", error);
    }
    
  });



module.exports = router;
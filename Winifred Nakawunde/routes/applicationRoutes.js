//introduce express
const express = require("express");

//Accesing the router function in express
const router = express.Router();

//introduce the model
const StudentApplication = require("../models/application");

router.get("/apply" , (req, res)=>{
    res.render('studentapplication.pug')
})

router.post("/apply", async(req, res) => {
    try {
    const student = new StudentApplication (req.body);
    console.log(student);
    await student.save();
    res.send("student registered")
    } catch (error) {
      res.status(400)
      console.log("error registering student", error)
    }
    
  });

  module.exports = router;
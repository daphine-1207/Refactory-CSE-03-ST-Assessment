const express = require("express");
const router = express.Router();
const moment = require('moment');

//importing model
 const FormModel = require("../models/formModel");

 

 //get form route
 router.get("/form", async (req, res) => {
    res.render("form");
 });


//  //post form route
router.post("/form",  async(req, res)=> {
  try {  
     const field = new FormModel(req.body);
     console.log(field);
     await field.save();
     
        res.redirect("/form");

  } catch (error) {
     res.status(400).send("Sorry something wrong!");
     console.log("error registering field...", error );
  }
});



 module.exports = router;
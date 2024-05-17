const express = require("express");
const router = express.Router();
const moment = require('moment');

//importing model
 const FormModel = require("./../models/formModule");

 

 //get form route
 router.get("/form", async (req, res) => {
    res.render("form");
 });


//  //post form route



 module.exports = router;
const express = require("express");
const router = express.Router();


const student = require('../models/Student');

router.get('/register', (req,res) => {
    res.render('applic');
})

router.post('/register', async(req,res) => {
try {
    const sstudent = new student(req.body); 
    console.log(sstudent); 
    await sstudent.save(); 
    res.redirect("/register"); 
} catch (error) {
  res.status(400).send('Sorry! something went wrong!')  
}
})


module.exports = router;
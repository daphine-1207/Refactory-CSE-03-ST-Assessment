const express = require('express');
const router = express.Router();

//import model
const  Registration = require('../models/registration');

// routes
router.get('/registration', (req, res) => {
  res.render('registration')
});
// initialising the async function
router.post("/registration", async(req, res) => {
    // req.body means all the data in our body 
    try {
      const person = new Registration(req.body)
    console.log(person)
    await person.save()
    // res.send('Registration successful.')
    res.redirect('/registration')
    } catch (error) {
      res.status(400).send('Sorry! Something went wrong')
      console.log('Error in registration...',error)
    }
    
  });
// export default router;

module.exports = router
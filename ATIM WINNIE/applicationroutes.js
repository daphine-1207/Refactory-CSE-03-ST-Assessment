const express = require('express');
const router = express.Router();
const Application = require('../models/Application');

// Render application form
router.get('/', (req, res) => {
  res.render('application_form');
});

// Handle form submission
router.post('/', async (req, res) => {
  try {
    const application = new Application(req.body);
    await application.save();
    res.redirect('/application/success');
  } catch (error) {
    res.status(400).send('Error saving application: ' + error.message);
  }
});

// Success page
router.get('/success', (req, res) => {
  res.render('success');
});

module.exports = router;

const express = require('express');
const router = express.Router();
const Form = require('../Models/Form');

// Render the form page
router.get('/form', (req, res) => {
    res.render('form'); 
    
});

// Handle form submission
router.post('/form', async (req, res) => {
    try {
        const formData = req.body; 
        const newFormEntry = await Form.create(formData);
        console.log("New form entry:", newFormEntry); 
        res.status(201).json({ message: 'Registration successful!', data: newFormEntry });
    } catch (error) {
        console.error("Error submitting form:", error);
        res.status(500).json({ message: 'An error occurred while processing your request.' });
    }
});

module.exports = router;

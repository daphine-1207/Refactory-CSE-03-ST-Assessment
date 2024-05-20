const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/submit', (req, res) => {
    const { firstName, lastName, email, phone, gender } = req.body;

    // Validate the input data
    if (!firstName || !lastName || !email || !phone || !gender) {
        return res.status(400).json({ error: 'Please fill in all fields' });
    }

    // Process the data (e.g. save to database, send email, etc.)
    console.log(`Received submission: ${firstName} ${lastName} ${email} ${phone} ${gender}`);

    // Return a success response
    res.json({ message: 'Form submitted successfully' });
});

app.listen(3000, () => {
    console.log('Server listening on port 3000');
});

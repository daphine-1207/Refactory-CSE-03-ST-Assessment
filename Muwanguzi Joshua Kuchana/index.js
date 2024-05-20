const express = require('express');
const app = express();


const session= require('express-session');
const passport= require('passport');
const mongoose = require("mongoose");

require('dotenv') .config();

const path = require('path');








// For invalid routes
app.get('*', (req, res) => {
    res.send('404! This is an invalid URL.');
});


app.listen(3000, () => console.log('Asses listening on port 3000!'));
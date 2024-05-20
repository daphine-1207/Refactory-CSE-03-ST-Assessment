// Server dependencies
const express = require('express');
const path = require('path');
const mongoose = require('mongoose')

// Initialize our app
const app = express();

// Set our poth for public files
app.use(express.static(path.join(__dirname, './public')));

// Import enviroment variables
require('dotenv').config();

// Add pug configuration
require('pug');
app.set('view engine', 'pug');

// Manage incoming data
app.use(express.json({extended: false}));
app.use(express.urlencoded({extended: true}));

// Database connection
mongoose
.connect(process.env.DATABASE, {})
.then(() => console.log('connected to database'))
.catch(() => console.log('database connection failed'))

// Routes
app.use('/', require('./routes/mainRoutes.js'));

// Run the Server on the designated port
app.listen( process.env.PORT, () => {
    console.log(`server running on port ${process.env.PORT}`)
})
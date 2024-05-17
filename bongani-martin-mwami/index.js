// Dependencies
const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const path = require('path');
const passport = require('passport'); 
const expressSession = require("express-session")({
    secret:"secret",
    resave:false,
    saveUninitialized:false
})
  
require('dotenv').config();

// Import Routes
const registrationRoutes = require('./routes/registrationRoutes')

// Instantiations
const app = express();
const port = 3100;

// Configurations
mongoose.connect(process.env.DATABASE, {
    useNewUrlParser:true,
    useUnifiedTopology:true
});
mongoose.connection
.once('open', () => {
    console.log('Mongoose connection successful')
})
.on('error', () => {
    console.log(`Connection error: ${error, message}`)
});

app.set('view engine', 'pug');
app.set('views', path.join(__dirname, 'views'));

// Middleware
app.use(express.static(path.join(__dirname, 'public')))
app.use(express.urlencoded ({extended:true}));
app.use(express.json());
app.use(cors());

// Express Session Configs
app.use(expressSession); 
app.use(passport.initialize());
app.use(passport.session()); 

// Routes
app.use('/', registrationRoutes);

// Invalid Routes
app.get('*', (req, res) => {
    res.send('404! Page not found')
});

// Boostrapping Routes
app.listen(port, () => console.log(`Listening on ${port}`));
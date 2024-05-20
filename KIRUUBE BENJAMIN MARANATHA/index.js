//Dependencies
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const path = require('path');
const passport = require('passport');
const expressSession = require("express-session")({
    secret:"secret",
    resave:false,
    saveUninitialized:false
})

require('dotenv').config();

//Instantiations
const app = express();
const port = 4001;

//Import Routes
const studentRoutes = require('./routes/student')

//Configuration
mongoose.connect(process.env.DATABASE, {
    useNewUrlParser:true,
    useUnifiedTopology:true
});
mongoose.connection
.once('open', () => {
    console.log('Mongoose connected successfully');
})
.on('error', err => {
    console.log(`Connection error: ${err. message}`);
});

app.set('view engine', 'pug');
app.set(path.join(__dirname, 'views'));

//Middleware
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({extended:true}));
app.use(express.json());
app.use(cors());

app.use(expressSession); 
app.use(passport.initialize());
app.use(passport.session()); 


//Routes
app.use('/', studentRoutes);


//Invalid Routes
app.use('*', (req,res) => {
   res.send('404! This page does not exist..')
});

// Bootstrapping
app.listen(port, () => console.log(`Listening on ${port}`))
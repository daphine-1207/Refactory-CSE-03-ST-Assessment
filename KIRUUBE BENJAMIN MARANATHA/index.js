//Dependencies
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

//Instantiations
const app = express();
const port = 4001;

//Configuration
mongoose.connect(process.env.DATABASE, {
    useNewUrlParser:false,
    useUnifiedTopolgy:false,
});
mongoose.connection
.once('open', () => {
    console.log('Mongoose connected successfully');
})
.on('error', err => {
    console.log(`Error message: ${err, message}`);
});

//Middleware
app.use(express.urlencoded({extended:true}));
app.use(express.json());
app.use(cors());

//Routes


//Invalid Routes
app.use('*', (res,req) => {
   res.send('404! This page does not exist..')
});

// Bootstrapping
app.listen(port, () => console.log(`Listening on ${port}`))
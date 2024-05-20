// console.log('hello');
// dependencies
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const path = require('path');


require('dotenv').config();
// instatiations
const app = express();
const port = 3000;

const registration = require('./models/registration');

// importin route
const registrationRoute = require('./routes/registrationRoute');
// configurations
mongoose.connect(process.env.DATABASE,{
    useNewUrlParser: true,
    useUnifiedTopology: true, 
  });
  
  mongoose.connection
    .once("open", () => {
      console.log("Mongoose connection open");
    })
    .on("error", err => {
      console.error(`Connection error: ${err.message}`);
   });

   app.set('view engine', 'pug');
   app.set('views', path.join(__dirname, 'views'));

  //  middleware
  app.use(express.urlencoded({extended:true}));
  app.use(express.json());
  app.use(cors());

// use our imported route
app.use('/', registrationRoute);
  // routes
app.get('registration', (req,res) => {
  res.sendFile(__dirname + '/registration.html')
});
app.post('registration', (req,res)=>{
  res.send('success')
});

  // invalid routes
  app.get('*', (req, res) => {
    res.send('404! This is an invalid URL.');
  });



app.listen(port, () => console.log(`listening on ${port}`));
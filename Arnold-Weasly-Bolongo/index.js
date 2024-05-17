// dependency
const express = require('express'); // for posting
const mongoose = require('mongoose'); // for mongodb
const path = require('path'); //for pug
const passport = require('passport'); //for passport
const moment = require('moment'); //for moment
const expressSession = require('express-session')({ // for express-session
  secret:"secret",
  resave: false,
  saveUninitialized: false
});

require("dotenv").config();


/**
 *! //routes
 */


const port = process.env.port || 3800  // listening to port



//impoting Routes
const dataFormRoutes = require("./routes/formRoute");



//instantiation
const app = express();


//configuration
 mongoose.connect(process.env.DATABASE, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

mongoose.connection
  .once("open", () => {
    console.log("mongodb connection successfully open");
  })
  .on("error", err => {
    console.error(`Connection error: ${err.message}`);
 });


 app.locals.moment = moment;

 app.set("view engine", "pug"); // setting the view engine to pug
 app.set("views", path.join(__dirname, "views")); //specify the directory where the views are found

 

//routes
/**
 *! Middleware
 */
app.use(express.static(path.join(__dirname, "public")))// for static files in dir public
app.use("/public/images/uploads", express.static(__dirname +"/public/images/uploads"));

app.use(express.urlencoded({extended: true}));
app.use(express.json());

//Express session  configurations
app.use(expressSession);
app.use(passport.initialize());
app.use(passport.session());



/**
 *! Use imported routes from above
 */

//use imported route
app.use("/", dataFormRoutes);




  // For invalid routes
app.get('*', (req, res) => {
  res.send('404! This is an invalid URL.');
});

  //always the last line in the code!!!
app.listen(port, () => console.log(`listening on port ${port}`));




//read about https status codes
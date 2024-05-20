//dependecies
const express = require("express"); // for posting
const mongoose = require("mongoose"); //for mongodb
const path = require("path"); 
const passport = require("passport");
const moment = require("moment")
const expressSession = require("express-session")({
  secret:"secret", 
  resave:false,
  saveUninitialized:false
});

require("dotenv").config();
const port = 3502;

// //import register model with user details
// const registration =require("./models/preci")


//import route
const preciRoutes = require("./routes/preciRoutes");

// const feedbackRoutes= require("./routes/feedbackRoutes")
//instantiations
const app = express();

//configgurations
mongoose.connect(process.env.DATABASE,);

mongoose.connection
  .once("open", () => {
    console.log("Mongoose connection successfully open");
  })
  .on("error", (err) => {
    console.error(`Connection error: ${err.message}`);
  });

  app.locals.moment = moment
//  setting the view engine
app.set("view engine", "pug");
app.set("views", path.join(__dirname, "views")); //specify the directory where the views are found

//middleware
app.use(express.static(path.join(__dirname, "public"))); //set directory for static files
app.use("/public/images/uploads", express.static(__dirname +"/public/images/uploads"));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

//expressSession configs
app.use(expressSession);
app.use(passport.initialize());
app.use(passport.session());

//passport configs
passport.use(registration.createStrategy());
passport.serializeUser(registration.serializeUser());
passport.deserializeUser(registration.deserializeUser());


//Route
app.get("/registerstudent", (req, res) => {
  res.render("preci");
});

//use imported routes
app.use("/", preciRoutes);



// For invalid routes
app.get("*", (req, res) => {
  res.send("404! This is an invalid URL.");
});

// Always the last line
app.listen(port, () => console.log(`listening on port ${port}`)); // new

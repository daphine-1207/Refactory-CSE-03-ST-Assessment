require('dotenv').config(); // Load environment variables from .env file

// Dependencies
const express = require("express");
const mongoose = require("mongoose");
const path = require("path");
const Form = require("./Models/Form"); // Assuming Form is your model
const formroute = require("./routes/formroute");

// Port
const port = 3002;

// Express app
const app = express();

//Configgurations
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
// View engine setup
app.set("view engine", "pug");
app.set("views", path.join(__dirname, "views"));

// Middleware
app.use(express.static(path.join(__dirname, "public")));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Routes
app.use("/", formroute); // Assuming formroute is the router for handling form-related routes

// Invalid routes
app.get("*", (req, res) => {
  res.send("404! This is an invalid URL.");
});

// Start the server
app.listen(port, () => console.log(`Listening on port ${port}`));

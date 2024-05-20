// Dependencies
const express = require("express");
const mongoose = require("mongoose");
const path = require("path"); //for pug

require("dotenv").config();

const port = 4800;

//Importing routes
const registrationRoutes = require("./routes/studentApplicationRoutes");


// Instantiations;
const app = express();

// Configarations
mongoose.connect(process.env.DATABASE, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

mongoose.connection
  .once("open", () => {
    console.log("Mongoose connection open");
  })

  .on("error", (err) => {
    console.error(`Connection error: ${err.message}`);
  });

app.set("view engine", "pug"); //setting the view engine to pug
app.set("views", path.join(__dirname, "views")); //specify the directory where the views are found

// Middleware
app.use(express.static(path.join(__dirname, "public"))); //set directory for static files
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
/*
// Express session configurations

// passpert configs

*/
// Use imported routes
app.use("/", registrationRoutes);


// For invalid routes
app.get("*", (req, res) => {
  res.send("404 Invalid URL");
});

// Bootstrapping the server
app.listen(port, () => console.log(`listening on port ${port}`));

// introducing mongoose to the model
const mongoose = require("mongoose");

// Access the schema function in mongoose
const Schema = mongoose.Schema;

// Using the function to create the schema.

const studentRegisterSchema = new Schema({
 
  firstName: {
    type: String,
    trim: true,
  },
  lastName: {
    type: String,
    trim: true,
  },
  course: {
    type: String,
    trim: true,
  },
  entryScheme: {
    type: String,
    trim: true,
  },
  intake: {
    type: String,
    trim: true,
  },
  sponsorship: {
    type: String,
    trim: true,
  },
  gender: {
    type: String,
    trim: true,
  },
  dateOfBirth: {
    type: String,
    trim: true,
  },
  residence: {
    type: String,
    trim: true,
  },
 
});


module.exports = mongoose.model("Application", studentRegisterSchema);

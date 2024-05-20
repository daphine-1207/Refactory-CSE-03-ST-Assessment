const mongoose = require('mongoose');

const ApplicationSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  course: { type: String, required: true },
  dob: { type: Date, required: true },
  address: { type: String, required: true }
});

module.exports = mongoose.model('Application', ApplicationSchema);

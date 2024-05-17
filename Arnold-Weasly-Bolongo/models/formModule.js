const mongoose = require("mongoose");
const moment = require('moment');

const formSchema = new mongoose.Schema({
    firstName:{
        type: String, 
        trim: true
    },
    dob:{
        type: Date,
        trim: true
    },
    lastName:{
        type: String, 
        trim: true
    },
    gender:{
        type: String, 
        trim: true
    },
    course:{
        type: String, 
        trim: true
    },
    entryScheme:{
        type: String, 
        unique: true
    },
    residence:{
        type: String, 
        trim: true
    },
    intake:{
        type: String, 
        trim: true
    },
    sponsorship:{
        type: Number, 
        trim: true
    }
});

module.exports = mongoose.model("StudentForm", formSchema)

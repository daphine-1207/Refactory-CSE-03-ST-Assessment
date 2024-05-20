const mongoose = require('mongoose');

const { Schema } = mongoose;

const studentSchema = new Schema({
    firstName:{
        type: String,
        required: true,
        minlength: 3,
        maxlength: 50
    },
    lastName:{
        type: String,
        required:true,
        minlength: 3,
        maxlength: 50
    },
    course:{
        type: String,
        required:true,
    },
    entryScheme:{
        type: String,
        required:true,
    },
    intake:{
        type: String,
        required:true,
    },
    sponsorship:{
        type: String,
        required:true,
    },
    gender:{
        type: String,
        required:true,
    },
    dateOfBirth:{
        type: String,
        required:true,
    },
    residence:{
        type: String,
        required:true,
    },
});

module.exports = mongoose.model( 'Student',  studentSchema);
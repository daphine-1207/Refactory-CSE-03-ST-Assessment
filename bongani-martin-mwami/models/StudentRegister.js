const mongoose = require('mongoose');

const studentRegSchema = new mongoose.Schema ({
    firstName: {
        type:String,
        trim:true
    },
    lastName: {
        type:String,
        trim:true
    },
    course: {
        type:String,
        trim:true
    },
    entryScheme: {
        type:String,
        trim:true
    },
    intake: {
        type:String,
        trim:true
    },
    sponsorship: {
        type:String,
        trim:true
    },
    gender: {
        type:String,
        trim:true
    },
    dateOfBirth: {
        type:String,
        trim:true
    },
    residence: {
        type:String,
        trim:true
    }
});

module.exports = mongoose.model('StudentRegister', studentRegSchema);
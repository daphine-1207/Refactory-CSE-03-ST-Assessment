const mongoose = require("mongoose");
const StudentSchema = new mongoose.Schema({
    firstName:{
        type:'String',
        trim:true
    },
    lastName:{
        type:'String',
        trim:true
    },
    course:{
        type:'String',
        trim:true
    },
    entryScheme:{
        type:'String',
        trim:true
    },
    intake:{
        type:'String',
        trim:true
    },
    scholarship:{
        type:'String',
        trim:true
    },
    inlineRadioOptions:{
        type:'String',
        enum:['male', 'female'],
        trim:true
    },
    dob:{
        type:'String',
        trim:true
    },
    residency:{
        type:'String',
        trim:true
    }


})
module.exports = mongoose.model("Student", StudentSchema);
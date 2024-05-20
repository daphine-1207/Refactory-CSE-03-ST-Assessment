const mongoose = require("mongoose");

const applicationschema = new mongoose.Schema({
    firstname:{
        type:String,
        trim:true
    },
    lastname:{
        type:Date,
        trim:true,
    },
    
    course:{
        type:String,
        trim:true,
    },
    entryscheme:{
        type:String,
        trim:true,
    },
    intake:{
        type:String,
        trim:true,
    },
    scholarship:{
        type:String,
        trim:true,
    },
    gender:{
        type:String,
        trim:true,
    },
   dateOfBirth:{
    type:String,
    trim:true,
},
   residence:{
    type:String,
    trim:true,
}

});

module.exports = mongoose.model("Application" , applicationschema)
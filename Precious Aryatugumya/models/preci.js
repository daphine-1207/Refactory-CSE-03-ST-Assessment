const mongoose = require("mongoose");

const registrationSchema = new mongoose.Schema( {
  firstName:{
    type:String,
    trim:true
  }, 
  lastName:{
    type:String,
    trim:true
  } , 
  course:{
    type:String,
    trim:true
  }, 
  entryScheme:{
    type:Date,
    trim:true
  }, 
  intake:{
    type:String,
    trim:true
  },   
  sponsorship:{
    type:String,
    trim:true
  },
  gender:{
    type:String,
    trim:true
  },  
  dob:{
    type:String,
    trim:true
  }, 
 residence:{
    type:Number,
    trim:true
  },
  agreeTerms:{
    type:String,
    trim:true
  }  

});


module.exports = mongoose.model("preci",registrationSchema )
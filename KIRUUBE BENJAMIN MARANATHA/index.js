//Dependencies
const express = require('express');

//Instantiations
const app = express();
const port = 4001;

//Configuration

//Middleware
app.use(express.urlencoded({extended:true}));

//Routes


//Invalid Routes
app.use('*', (res,req) => {
   res.send('404! This page does not exist..')
});

// Bootstrapping
app.listen(port, () => console.log(`Listening on ${port}`))
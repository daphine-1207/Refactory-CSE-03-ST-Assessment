//dependecy
const express = require('express');



//instatiations
const app = express();
app.get('/', (req, res) => { // new
  res.send('Student form');
});

app.get('/about', (req, res) => { // new
    res.send('student forms.');
  });



//bootstrap the server
app.listen(3000, () => console.log('listening on port 3000'));
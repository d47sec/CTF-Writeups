const http = require('http');
const si = require('systeminformation');
var grabzit = require('grabzit');
var client = new grabzit("MDQxNjRjYTQxNzk3NDI2MDk4MWVjNzE3MWZhNmVhODY=", "dWA/Pz9aTmodNz8/Y3EWDC4/P3Q/P0JKP2I/P0J6Dz8=");
var options = { "browserHeight": -1, "width": -1, "height": -1 };

var express = require('express');
var app = express();

app.use(express.static(__dirname+'/public'));

const port = 8787;

app.get('/CaptureSite', (req, res) => {
  const queryData = req.query.url
  console.log(queryData);
  if(queryData == undefined){
    res.sendFile(__dirname + '/index.html');
  }
  si.inetChecksite(queryData).then((data) => { // BUG ở dòng này
    console.log(data.status);
    if (data.status == 200) {
      client.url_to_image(queryData, options);
      client.save_to(__dirname+'/public/images/result.jpg', function (error, id) {
        if (error != null) {
          throw error;
        } else{
          console.log("Successfully")
          res.sendFile(__dirname + '/index.html');
        }
      });
    }
  });
});

app.listen(port, () => console.log('Listening on port 8787...'))



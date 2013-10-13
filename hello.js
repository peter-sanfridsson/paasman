var http = require('http');
//var process = require('process');
var server = http.createServer(function (request, response) {
    response.writeHead(200, {"Content-Type": "text/plain"});
    response.end("Hello World\n");
});

server.listen(process.argv[2] || 8123);

//server.listen(8123);
/*
console.log("hello, server is started!");

setInterval(function() {
    console.log("tick tick tick");
}, 1000);
*/

//var http = require("http");
//var app = require("./appname/file.js");

//app.listen(8000);

/*
setInterval(function() {
    console.log("tell master I'm alive!");
}, 1000*30); // every 30 seconds
*/
var http = require("http");

var server = http.createServer(function(request, response){
	console.log("Request made");
	response.write("Welcome!");
	response.end;
});

server.listen("3000");

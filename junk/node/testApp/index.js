var express = require("express");
var path = require("path");
var app = express();

app.use(express.static("static"));
app.use(logErr);

function logErr(err, rq, rs, next){
	console.error(err.stack);
	next(err);
};

app.get('/', function(rq, rs) {
	rs.sendFile(path.join(__dirname + "/index.html"));
});

app.listen(3000, function() {
	console.log("Listening on port 3000");
});

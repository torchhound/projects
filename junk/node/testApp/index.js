var express = require("express"),
	path = require("path"),
	morgan = require("morgan"),
	port = process.env.PORT || 3000,
	app = express();

app.use(morgan("dev"));
app.use(express.static("static"));
app.use(logErr);

function logErr(err, rq, rs, next){
	console.error(err.stack);
	next(err);
};

app.listen(port, function() {
	console.log("Listening on port 3000");
});

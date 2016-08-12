import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	'''renders the index template and produces a random number for the dice roll'''
	max = request.form['text']
	if request.method == "POST":
		try:
			rng = random.randint(1,max)
			return render_template("index.html", rng = rng)
		except Exception as e:
			return render_template("index.html", rng = e)
	elif request.method == "GET":
		return render_template("index.html")

if __name__ == "__main__":
	app.run()

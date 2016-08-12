import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	'''renders index.html'''
    return render_template("index.html")

@app.route("/", methods=["POST"])
def indexPost():
	'''renders the index template and produces a random number for the dice roll'''
	max = request.form['text']
	try:
		rng = random.randint(1,max)
		return render_template("index.html", rng = rng)
	except Exception as e:
		return render_template("index.html", rng = e)

if __name__ == "__main__":
	app.run()

from flask import *
import pandas as pd

app = Flask(__name__)




@app.route("/")
def one():
	return render_template("aspergillosis_in_cats.html")

@app.route("/2")
def two():
	return render_template("blastomycosis_in_cats.html")

@app.route("/3")
def three():
	return render_template("histoplasmosis_in_cats.html")

@app.route("/4")
def four():
	return render_template("coccidioidomycosis_in_cats.html")

@app.route("/5")
def five():
	return render_template("malassezia pachydermatis_in_cats.html")

@app.route("/6")
def six():
	return render_template("pneumocystosis_in_cats.html")

@app.route("/7")
def eight():
	return render_template("sporotrichosis_in_cats.html")


if __name__ == "__main__":
    app.run(debug=True)

#topres('delhi')


from flask import Flask, request, render_template
from flask_cors import cross_origin
app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
	return render_template("index.html")



@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def submit():
    if request.method == "POST":
        if request.form.get("single"):
            single_inheritance()
        elif request.form.get("multiple"):
            multiple_inheritance()
        elif request.form.get("multi"):
            multi_inheritance()
        elif request.form.get("hierarical"):
            hierarical_inheritance
        elif request.form.get("hybrid"):
            hybrid_inheritance()
def single_inheritance():
    return render_template("singleinheritance.html")


def multi_inheritance():
    return render_template("multiinheritance.html")

def multiple_inheritance():
    return render_template("multipleinheritance.html")

def hierarical_inheritance():
    return render_template("hieraricalinheritance.html")

def hybrid_inheritance():
    return render_template("hybridinheritance.html")

if __name__ == "__main__":
	app.run(debug=True)

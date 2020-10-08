from flask import Flask, request, redirect, url_for, render_template



app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def home():
    return render_template("home.html")



@app.route("/vaardigheden", methods=["GET","POST"])
def vaardigheden():
    return render_template("vaardigheden.html")




@app.route("/projecten", methods=["GET","POST"])
def projecten():
    return render_template("projecten.html")




@app.route("/lol", methods=["GET","POST"])
def lol():
    return render_template("lol.html")



if __name__ == "__main__":
    app.run()
    app.debug = True



import pickle
import sklearn
import numpy as np
from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "CSCI626"
# use timedelta to let the session store data for 2 days or 30 mins
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/")
def home():
    return render_template("index.html")
    #return render_template("index.html", content=name, r=2)

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        category = request.form['cate']
        review = request.form["rv"]
        #predict
        category = category.replace(" ", "_")
        filename = category + "_yelp_review_predict_star.pkl"
        infile = open(filename, "rb")
        model = pickle.load(infile)
        infile.close()
        review_rating = model.predict([review])

        session["review"] = {'Category': category,
                            'Review': review,
                            'Predict rating': int(review_rating[0])}
        return redirect(url_for("review"))
    else:
        if "review" in session:
            return redirect(url_for("review"))
        return render_template("login.html")
@app.route("/review")
def review():
    if "review" in session:
        review = session["review"]
        return f"<h1>Category:{review.get('Category')}</h1>\n<h2>Review:{review.get('Review')}</h2>\n<h1>Rating:{review.get('Predict rating')}</h1>"
    else:

        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("review", None)
    return redirect(url_for("login"))


# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"
#
# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run(debug=True)
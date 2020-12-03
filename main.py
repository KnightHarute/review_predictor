import pickle
import sklearn
import numpy as np
from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from datetime import timedelta

app = Flask(__name__,
            static_folder="./static",
            template_folder="./")

app.secret_key = "CSCI"
# use timedelta to let the session store data for 2 days or 30 mins
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/sub", methods=["POST", "GET"])
def sub():
    print(request.get_json(silent=True))
    category = request.get_json(silent=True).get("category")
    category = category.replace(" ", "_")
    review = request.get_json(silent=True).get("review")
    filename = category + "_yelp_review_predict_star.pkl"
    infile = open(filename, "rb")
    model = pickle.load(infile)
    infile.close()
    review_rating = model.predict([review])
    return jsonify(int(review_rating[0]))


if __name__ == "__main__":
    app.run(port=4455, debug=True)

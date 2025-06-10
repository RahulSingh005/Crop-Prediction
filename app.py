import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

flask_app = Flask(__name__, template_folder="templates")
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)[0].capitalize()
    return render_template("index.html", prediction_text=f"The Predicted Crop is {prediction}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)

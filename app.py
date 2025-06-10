import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

app = Flask(__name__, template_folder="templates")  # Changed from flask_app to app
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")  # Changed from flask_app to app
def Home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])  # Changed from flask_app to app
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)[0].capitalize()
    return render_template("index.html", prediction_text=f"The Predicted Crop is {prediction}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)  # Changed from flask_app to app

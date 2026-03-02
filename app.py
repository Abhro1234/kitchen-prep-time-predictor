from flask import Flask, render_template, request, jsonify
from predictor import predict_kpt
from signal_engine import enrich_signals

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    enriched = enrich_signals(data)

    prediction = predict_kpt(enriched)

    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)
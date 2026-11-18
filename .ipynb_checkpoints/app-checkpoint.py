import joblib
import numpy as np
from preprocess import process_review
from flask import Flask, request, jsonify


app=Flask(__name__)
model=joblib.load('model.joblib') #Loading the saved model
vectorizer=joblib.load('vectorizer.joblib') # Loading the saved TF-IDF vectorizer


@app.route("/predict", methods=["POST"])  # Whenever user POSTs data to "/predict", call this function.
def predict():
    data = request.get_json()  # Reading the incoming JSON data.
    
    reviews = data['reviews']  # Extract the review from the dictionary
    
    process_rev = process_review(reviews)  # Preprocess the review posted
    
    process_rev = vectorizer.transform([process_rev])  # Extract features from the review

    prediction=model.predict(process_rev) # predict the sentiment

    return jsonify({"prediction":"positive" if prediction[0]=='1' else "negative"}) # output  the sentiment jsonify is used to convert the python dict into JSON object

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status":"ok"})

if __name__ == "__main__":
     import os
     app.run(host="127.0.0.1",port=int(os.environ.get("PORT",5000)))
     
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Chargement du modèle préalablement entraîné
knn_model = joblib.load('knn_model.joblib')

# Endpoint pour les prédictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = knn_model.predict([data['data']])
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(port=5000)

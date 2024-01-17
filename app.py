from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Charger le modèle
model = joblib.load('iris_knn_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get('features')
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)

''' command line to test '''
# curl -X POST -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}' http://127.0.0.1:5000/predict

'''
{
  "prediction": 0
}
'''
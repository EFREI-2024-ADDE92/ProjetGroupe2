from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Charger le modèle
model = joblib.load('iris_knn_model.joblib')

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     features = data.get('features')
#     prediction = model.predict([features])
#     return jsonify({'prediction': int(prediction[0])})

@app.route('/predict', methods=['GET'])
def predict():
    features_str = request.args.get('features')
    features = [float(value) for value in features_str.split(',')]
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

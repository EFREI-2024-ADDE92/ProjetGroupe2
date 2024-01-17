from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

<<<<<<< HEAD
model = joblib.load('knn_model.joblib')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        # Traitement des paramètres de la chaîne de requête pour une requête GET
        sepal_length = float(request.args.get('sepal_length'))
        sepal_width = float(request.args.get('sepal_width'))
        petal_length = float(request.args.get('petal_length'))
        petal_width = float(request.args.get('petal_width'))
    elif request.method == 'POST':
        # Traitement du corps JSON pour une requête POST
        data = request.get_json(force=True)
        sepal_length = float(data['sepal_length'])
        sepal_width = float(data['sepal_width'])
        petal_length = float(data['petal_length'])
        petal_width = float(data['petal_width'])
    else:
        return jsonify({"error": "Method not allowed"}), 405

    features = [sepal_length, sepal_width, petal_length, petal_width]
    prediction = model.predict([features])
    return jsonify(prediction.tolist())

if __name__ == '__main__':
=======
# Charger le modèle
model = joblib.load('iris_knn_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get('features')
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    # app.run(debug=True)
>>>>>>> 62f2a3d9e2cc7fbddaecc901c2dbef5399d7d99f
    app.run(host='0.0.0.0', port=5000)

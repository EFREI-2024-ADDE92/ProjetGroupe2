from flask import Flask, request, jsonify
import joblib
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import time
app = Flask(__name__)

model = joblib.load('iris_knn_model.joblib')


app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

REQUEST_COUNT = Counter(
    'app_request_count',
    'Application Request Count',
    ['method', 'endpoint', 'http_status']
)
REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Application Request Latency',
    ['method', 'endpoint']
)
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    start_time = time.time()
    REQUEST_COUNT.labels('GET', '/', 200).inc()
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

    mapping_labels = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    label = mapping_labels[prediction[0]]
    REQUEST_LATENCY.labels('GET', '/').observe(time.time() - start_time)
    return jsonify(f"Prediction: {label}")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
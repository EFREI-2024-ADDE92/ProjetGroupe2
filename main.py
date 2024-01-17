# Import des bibliothèques
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import joblib

# Chargement du dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Entraînement du modèle
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

# Évaluation du modèle
accuracy = knn_model.score(X_test, y_test)
print(f"Accuracy du modèle : {accuracy}")

# Exportation du modèle
joblib.dump(knn_model, 'knn_model.joblib')

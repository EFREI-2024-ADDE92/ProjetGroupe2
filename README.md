# ProjetGroupe2

## Endpoint de l'API
Pour faire des prédictions avec l'API, utilisez l'endpoint suivant en envoyant une requête POST avec des données d'Iris au format JSON.

### Guide d'usage :
```
curl -X POST \
    https://adde92-gr2-container.blackcoast-633d2335.francecentral.azurecontainerapps.io/predict \
    -H 'Content-Type: application/json' \
    -d '{"features": [<your-sepal-length>, <your-sepal-width>, <your-petal-length>, <your-petal-width>]}'
```

Example :
```
curl -X POST \
    https://adde92-gr2-container.blackcoast-633d2335.francecentral.azurecontainerapps.io/predict \
    -H 'Content-Type: application/json' \
    -d '{"features": [1.2, 1.5, 1.7, 5]}'
```


### Test de charge avec K6
Pour réaliser un test de charge et évaluer les performances de l'API sous différentes conditions, utilisez l'outil k6.
```
k6 run -e MY_URL=https://votre_url/ <your-test-file>.js
```
Example :
```
k6 run -e MY_URL=https://adde92-gr2-container.blackcoast-633d2335.francecentral.azurecontainerapps.io/ testcharge.js
```

Ces commandes vous permettront d'utiliser l'API, faire des prédictions et réaliser des tests de charge pour évaluer les performances du système.



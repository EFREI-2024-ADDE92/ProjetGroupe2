# ProjetGroupe2

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


### Test de charge
```
k6 run -e MY_URL=https://votre_url/ <your-test-file>.js
```
Example :
```
k6 run -e MY_URL=https://adde92-gr2-container.blackcoast-633d2335.francecentral.azurecontainerapps.io/ testcharge.js
```
import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 10,  // Nombre de VUs (utilisateurs virtuels)
  duration: '30s',  // Durée totale du test
};

export default function () {
  // Définissez l'URL de votre API
  const url = 'https://adde92-gr2-container.blackcoast-633d2335.francecentral.azurecontainerapps.io/predict';

  // Définissez les données JSON pour la requête POST
  const payload = {
    features: [1.2, 1.5, 1.2, 5]
  };

  // Définissez les en-têtes de la requête
  const headers = {
    'Content-Type': 'application/json'
  };

  // Envoyez la requête POST avec les données JSON
  const response = http.post(url, JSON.stringify(payload), { headers: headers });

  // Ajoutez une pause (simulation d'une charge constante)
  sleep(1);
}

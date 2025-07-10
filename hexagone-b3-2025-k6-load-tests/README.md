# k6

## Exercice HTTP

Commande pour générer le script avec le template par défaut

```bash
# Linux
docker run --rm -u $(id -u) -v "${PWD}:/app" -w /app  grafana/k6 new
# Windows
docker run --rm -v "${PWD}:/app" -w /app  grafana/k6 new
```

Commande pour exécuter le scénario inclus dans script.js

```bash
# Linux/OSX
docker run --rm  -i   grafana/k6 run - <script.js
# Windows Power Shell
cat script.js | docker run --rm  -i   grafana/k6 run -
```

Commande pour exécuter le scénario inclus dans script.js avec le rapport Web

```bash
docker run --rm -u $(id -u) -i -e K6_WEB_DASHBOARD=true -e K6_WEB_DASHBOARD_EXPORT=html-report.html -v "${PWD}:/app" -w /app grafana/k6 run script.js 
```

## Exercice gRPC

1. Créer un script js de base
2. Récupérer le fichier `interface.proto` et le rendre accessible à notre script js
3. Implémenter un scénario de test qui appelle la fonction `SayHello` avec 2 paramètres différents : `Hexa` et `Gone`.
4. Une fois implémenté, réaliser un test smoke (à vous de choisir les bonnes valeurs de VUs). Unique contrainte : la ramp up, le plateau et la phase de descente doivent être présentes